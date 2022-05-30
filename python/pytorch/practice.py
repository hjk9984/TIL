import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda
import numpy as np
import torch.nn.functional as F

tmp = [[1,2, 3],[4, 5, 6]]

x = torch.tensor(tmp)
print(x)
x = torch.from_numpy(np.array(tmp, dtype=np.float64))
print(x)
x1 = torch.ones_like(x)
print(x1)

print(torch.cat([x, x], dim=1))
print(x @ x.T)
print(x.matmul(x.T))
print(x * x)


tmp2 = torch.ones(3)
n = tmp2.numpy()
print(tmp2, n)
tmp2 += 2
print(tmp2, n)

tmp2 = tmp2 + 1
print(tmp2, n)




#--------------------

train_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
    target_transform=Lambda(lambda y: torch.zeros(10).scatter_(0, torch.tensor(y), value=1))
)

loader = DataLoader(train_data, batch_size=64, shuffle=True)

class demo(nn.Module):
    def __init__(self):
        super(demo, self).__init__()
        self.linear_relu = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.BatchNorm1d(512),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.BatchNorm1d(512),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = torch.flatten(x, start_dim=1)
        logits = self.linear_relu(x)
        return logits

model = demo()

loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr= 1e-3)
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, 10)

for batch, (x, y) in enumerate(loader):
    pred = model(x)
    loss = loss_fn(pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if batch % 100 == 0:
        print(f"{batch} | Loss {loss.item():.5f}")
