import os
from lightning.pytorch import LightningDataModule, LightningModule, Trainer
import torch
from torch import nn
from torch.utils.data import DataLoader, random_split
from torch.nn import functional as F
from torchvision import datasets, transforms


class MNIST(LightningDataModule):
  def __init__(self, data_path: str = '.', batch_size: int = 32):
    super().__init__()
    self.data_path = data_path
    self.data_transform = transforms.Compose([
      transforms.Resize((32, 32)),
      transforms.ToTensor(),
    ])
    _train_data = datasets.MNIST(self.data_path, train=True, download=True, transform=self.data_transform)
    self.train_data, self.val_train = random_split(
        _train_data, [55000, 5000], generator=torch.Generator().manual_seed(37)
      )
    self.test_data = datasets.MNIST(self.data_path, train=False, transform=self.data_transform)
    self.batch_size = batch_size
  def train_dataloader(self):
    return DataLoader(self.train_data, batch_size=self.batch_size, shuffle=True, num_workers=4)
  def val_dataloader(self):
    return DataLoader(self.val_data, batch_size=self.batch_size, num_workers=4, persistent_workers=True)
  def test_dataloader(self):
    return DataLoader(self.test_data, batch_size=self.batch_size, num_workers=4, persistent_workers=True)
  def predict_dataloader(self):
    return DataLoader(self.test_data, batch_size=self.batch_size, num_workers=4, persistent_workers=True)


class LeNet5(LightningModule):
  def __init__(self, learning_rate: float = 0.0001):
    super().__init__()
    self.save_hyperparameters()
    self.conv1 = nn.Conv2d(1, 6, kernel_size=5, stride=1)
    self.conv2 = nn.Conv2d(6, 16, kernel_size=5, stride=1)
    self.conv3 = nn.Conv2d(16, 120, kernel_size=5, stride=1)
    self.fc1 = nn.Linear(120, 84)
    self.fc2 = nn.Linear(84, 10)
  def forward(self, x):
    x = F.tanh(self.conv1(x))
    x = F.avg_pool2d(x, 2, 2)
    x = F.tanh(self.conv2(x))
    x = F.avg_pool2d(x, 2, 2)
    x = F.tanh(self.conv3(x))
    x = x.view(-1, 120)
    x = F.tanh(self.fc1(x))
    x = self.fc2(x)
    return F.softmax(x, dim=1)
  def training_step(self, batch, batch_idx):
    x, y = batch
    y_hat = self(x)
    loss = F.cross_entropy(y_hat, y)
    self.log("train_loss", loss, on_epoch=True)
    return loss
  def validation_step(self, batch, batch_idx):
    x, y = batch
    y_hat = self(x)
    loss = F.cross_entropy(y_hat, y)
    self.log("valid_loss", loss, on_epoch=True)
    return loss
  def test_step(self, batch, batch_idx):
    x, y = batch
    y_hat = self(x)
    loss = F.cross_entropy(y_hat, y)
    self.log("test_loss", loss, on_epoch=True)
    return loss
  def predict_step(self, batch, batch_idx):
    x, _ = batch
    return self(x)
  def configure_optimizers(self):
    return torch.optim.Adam(self.parameters(), lr=self.hparams.learning_rate)


def pl_mnist_lenet5_main():
  data_path = os.path.join(os.path.dirname(os.getcwd()), 'data')
  datamodule = MNIST(data_path=data_path)
  model = LeNet5()
  trainer = Trainer(max_epochs=10)
  trainer.fit(model, datamodule=datamodule)
  trainer.test(datamodule=datamodule)
  trainer.validate(datamodule=datamodule)
  trainer.predict(datamodule=datamodule)


if __name__ == "__main__":
  pl_mnist_lenet5_main()
