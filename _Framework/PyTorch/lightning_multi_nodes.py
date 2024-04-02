# https://lightning.ai/docs/pytorch/stable/common/lightning_module.html#lightning-module
# https://lightning.ai/docs/pytorch/stable/clouds/cluster_intermediate_1.html
# RUN THIS CODE ON EACH NODES.

import os
import torch
from torch.utils.data import DataLoader
import lightning as L
from lightning.pytorch.demos import Transformer, WikiText2

os.environ['MASTER_ADDR'] = '' # IP ADDRESS OF MASTER NODE e.g. '192.168.0.0'
os.environ['MASTER_PORT'] = '' # PORT NUMBER OF MASTER NODE e.g. '12345'
os.environ['WORLD_SIZE'] = '' # TOTAL GPUS OF CLUSTER e.g. '2'
os.environ['NODE_RANK'] = '' # ORDER OF THE CURRENT NODE e.g. '0'

class LightningTransformer(L.LightningModule):
    def __init__(self, vocab_size):
        super().__init__()
        self.model = Transformer(vocab_size=vocab_size)
    def forward(self, inputs, target):
        return self.model(inputs, target)
    def training_step(self, batch, batch_idx):
        inputs, target = batch
        output = self(inputs, target)
        loss = torch.nn.functional.nll_loss(output, target.view(-1))
        return loss
    def configure_optimizers(self):
        return torch.optim.SGD(self.model.parameters(), lr=0.1)

dataset = WikiText2()
dataloader = DataLoader(dataset)
model = LightningTransformer(vocab_size=dataset.vocab_size)

trainer = L.Trainer(
    fast_dev_run=100,
    accelerator='gpu',
    devices=1, # NUMBER OF GPU IN CURRENT NODE
    num_nodes=2,
    strategy='ddp'
)
trainer.fit(
    model=model,
    train_dataloaders=dataloader
)
