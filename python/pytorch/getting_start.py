from turtle import down
from setuptools import sic
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

train_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
)

# dataloader wraps dataset as iterable
# and supports batch, sampling, shuffle
n_batch = 64
train_loader = DataLoader(train_data, batch_size=n_batch)
test_loader = DataLoader(test_data)

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device}")

# the layers are parameterized within neural network.
# when nn.Module is inherited, all of the fields are automately tracked
# so, all of the parameters can be accessed  by method parameters(), named_parameters()
class demo(nn.Module):
    def __init__(self):
        super(demo, self).__init__()
        self.flatten = nn.Flatten();
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.BatchNorm1d(512),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.BatchNorm1d(512),
            nn.Linear(512, 10)
        )
    
    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

if __name__ == "__main__":
    model = demo().to(device=device)
    print(model)
    x, y = next(iter(train_loader))
    print(x.shape, x.dtype)         #[] 
    print(y)                        #[9, 0, 0, 3, 0, 2] >> not one hot

    for name, param in model.named_parameters():
        print(f"Layer: {name} | size:{param.size()}")

    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)


    #train
    # loader has dataset attribute
    train_size = len(train_loader.dataset)
    for batch, (x, y) in enumerate(train_loader):
        x, y = x.to(device), y.to(device)

        pred = model(x)
        loss = loss_fn(pred, y)         # loss function returns tensor not int
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(x)
            print(f"loss: {loss:.5f} [{current}/{train_size}]")


    #test
    test_size = len(test_loader.dataset)
    num_batches = len(test_loader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for x, y in test_loader:
            x, y = x.to(device), y.to(device)
            pred = model(x)
            test_loss += loss_fn(pred, y).item()        # if you wanna get acc, you should use item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= test_size
    print(f"Test Error: acc:{100*correct:.3f}")
