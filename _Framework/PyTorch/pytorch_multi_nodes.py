# https://csm-kr.tistory.com/89

"""
torchrun \
--nnode={2, ... nodes} \
--nproc_per_node={1, 2, ... gpus} \
--node_rank={0, 1, ... order} \
--master_addr={master_address} \
--master_port={master_port} \
multi_nodes.py
"""

"""
python -m torch.distributed.launch \
--nnode={2, ... nodes} \
--nproc_per_node={1, 2, ... gpus} \
--node_rank={0, 1, ... order} \
--master_addr={master_address} \
--master_port={master_port} \
multi_nodes.py
"""

import argparse
import numpy as np
import os
import random
import time

import torch
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.optim.lr_scheduler import StepLR
from torch.utils.data import DataLoader
from torch.utils.data.distributed import DistributedSampler

from torchvision import transforms
from torchvision.datasets.cifar import CIFAR10
from torchvision.models import vgg11

def set_random_seeds(random_seed=0):
    torch.manual_seed(random_seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    np.random.seed(random_seed)
    random.seed(random_seed)

def get_args_parser():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--lr', type=float, default=0.01)
    parser.add_argument('--epoch', type=int, default=10)
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--global_rank', type=int, default=0)
    parser.add_argument('--vis_step', type=int, default=10)
    parser.add_argument('--num_workers', type=int, default=4)
    parser.add_argument("--local_rank", type=int, default=0)
    parser.add_argument('--world_size', type=int, default=0)
    parser.add_argument('--port', type=int, default=23456)
    parser.add_argument('--root', type=str, default='data')
    parser.add_argument('--start_epoch', type=int, default=0)
    parser.add_argument('--save_path', type=str, default='./save')
    parser.add_argument('--save_file_name', type=str, default='cifar_vgg')
    return parser

def main(opts):
	# 1. set random seeds
    set_random_seeds(random_seed=0)	
    # 2. initialization
    init_for_distributed(opts)
    # 3. visdom
    vis = None
    # 4. prepare dataset
    transform_train = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=(0.4914, 0.4822, 0.4465),
            std=(0.2023, 0.1994, 0.2010)
        ),
    ])
    transform_test = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=(0.4914, 0.4822, 0.4465),
            std=(0.2023, 0.1994, 0.2010)),
        ])
    train_set = CIFAR10(
        root=opts.root,
        train=True,
        transform=transform_train,
        download=True
    )
    test_set = CIFAR10(
        root=opts.root,
        train=False,
        transform=transform_test,
        download=True
    )
    train_sampler = DistributedSampler(
        dataset=train_set, shuffle=True
    )
    test_sampler = DistributedSampler(
        dataset=test_set, shuffle=False
    )

    train_loader = DataLoader(
        dataset=train_set,
        batch_size=int(opts.batch_size / opts.world_size),
        shuffle=False,
        num_workers=int(opts.num_workers / opts.world_size),
        sampler=train_sampler,
        pin_memory=True
    )
    test_loader = DataLoader(
        dataset=test_set,
        batch_size=int(opts.batch_size / opts.world_size),
        shuffle=False,
        num_workers=int(opts.num_workers / opts.world_size),
        sampler=test_sampler,
        pin_memory=True
    )
    # 5. model
    model = vgg11(pretrained=False)
    model = model.cuda(opts.local_rank)
    model = DDP(
        module=model,
        device_ids=[opts.local_rank]
    )
    # 6. criterion
    criterion = torch.nn.CrossEntropyLoss().to(opts.local_rank)

    # 7. optimizer
    optimizer = torch.optim.SGD(
        params=model.parameters(),
        lr=0.01,
        weight_decay=0.0005,
        momentum=0.9
    )
    # 8. scheduler
    scheduler = StepLR(
        optimizer=optimizer,
        step_size=30,
        gamma=0.1
    )
    if opts.start_epoch != 0:
        checkpoint = torch.load(
            os.path.join(
                opts.save_path,
                opts.save_file_name
            ) + '.{}.pth.tar'.format(opts.start_epoch - 1),
            map_location=torch.device('cuda:{}'.format(opts.local_rank))
        )
        model.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        scheduler.load_state_dict(checkpoint['scheduler_state_dict'])
        if opts.global_rank == 0:
            print('\nLoaded checkpoint from epoch %d.\n' % (int(opts.start_epoch) - 1))
    for epoch in range(opts.start_epoch, opts.epoch):
        # 9. train
        tic = time.time()
        model.train()
        train_sampler.set_epoch(epoch)
        for i, (images, labels) in enumerate(train_loader):
            images = images.to(opts.local_rank)
            labels = labels.to(opts.local_rank)
            outputs = model(images)
            optimizer.zero_grad()
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            for param_group in optimizer.param_groups:
                lr = param_group['lr']
            toc = time.time()
            if (i % opts.vis_step == 0 or i == len(train_loader) - 1):
                print(
                    'GPU[{0}] Epoch [{1}/{2}], Iter [{3}/{4}], Loss: {5:.4f}, LR: {6:.5f}, Time: {7:.2f}'.format(
                        opts.global_rank,
                        epoch,
                        opts.epoch,
                        i,
                        len(train_loader),
                        loss.item(),
                        lr,
                        toc - tic
                    )
                )
                if vis is not None and opts.local_rank == 0:
                    vis.line(
                        X=torch.ones((1, 1)) * i + epoch * len(train_loader),
                        Y=torch.Tensor([loss]).unsqueeze(0),
                        update='append',
                        win='loss',
                        opts=dict(
                            x_label='step',
                            y_label='loss',
                            title='loss',
                            legend=['total_loss']
                        )
                    )
        if opts.local_rank == 0:
            if not os.path.exists(opts.save_path):
                os.mkdir(opts.save_path)
            checkpoint = {
                epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'scheduler_state_dict': scheduler.state_dict()
            }
            torch.save(
                checkpoint,
                os.path.join(
                    opts.save_path, 
                    opts.save_file_name + '.{}.pth.tar'.format(epoch)
                )
            )
            print("save pth.tar {} epoch!".format(epoch))
            # 10. test
            model.eval()
            val_avg_loss = 0
            correct_top1 = 0
            correct_top5 = 0
            total = 0
            with torch.no_grad():
                for i, (images, labels) in enumerate(test_loader):
                    images = images.to(opts.local_rank)
                    labels = labels.to(opts.local_rank)
                    outputs = model(images)
                    loss = criterion(outputs, labels)
                    val_avg_loss += loss.item()
                    _, pred = torch.max(outputs, 1)
                    total += labels.size(0)
                    correct_top1 += (pred == labels).sum().item()
                    _, rank5 = outputs.topk(5, 1, True, True)
                    rank5 = rank5.t()
                    correct5 = rank5.eq(labels.view(1, -1).expand_as(rank5))
                    for k in range(5):  # 0, 1, 2, 3, 4, 5
                        correct_k = correct5[:k+1].reshape(-1).float().sum(0, keepdim=True)
                    correct_top5 += correct_k.item()
            accuracy_top1 = correct_top1 / total
            accuracy_top5 = correct_top5 / total
            val_avg_loss = val_avg_loss / len(test_loader)
            if vis is not None:
                vis.line(
                    X=torch.ones((1, 3)) * epoch,
                    Y=torch.Tensor([accuracy_top1, accuracy_top5, val_avg_loss]).unsqueeze(0),
                    update='append',
                    win='test_loss_acc',
                    opts=dict(
                        x_label='epoch',
                        y_label='test_loss and acc',
                        title='test_loss and accuracy',
                        legend=['accuracy_top1', 'accuracy_top5', 'avg_loss']
                    )
                )
            print("top-1 percentage :  {0:0.3f}%".format(correct_top1 / total * 100))
            print("top-5 percentage :  {0:0.3f}%".format(correct_top5 / total * 100))
            scheduler.step()
    return 0

def init_for_distributed(opts):
    opts.global_rank = int(os.environ['RANK'])
    opts.local_rank = int(os.environ['LOCAL_RANK'])
    opts.world_size = int(os.environ['WORLD_SIZE'])
    torch.cuda.set_device(opts.local_rank)
    if opts.global_rank is not None and opts.local_rank is not None:
        print("Use GPU: [{}/{}] for training".format(opts.global_rank, opts.local_rank))
    dist.init_process_group(backend="nccl")
    torch.distributed.barrier()
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'vgg11 cifar training',
        parents=[get_args_parser()]
    )
    opts = parser.parse_args()
    main(opts)
    
