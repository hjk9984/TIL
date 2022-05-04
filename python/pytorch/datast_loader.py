import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda
import matplotlib.pyplot as plt
import pandas as pd
import os

# dataset saves sample and label
# dataloader wraps datasets with iterable obj

# ToTensor converts ndarray or image into FloatTensor and normalize
# Lambda transform get lambda function
train_dataset = datasets.FashionMNIST(
    root="data",
    download=True,
    train=True,
    transform=ToTensor(),
    target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))
)

idx = torch.randint(len(train_dataset), size=(1,))
img, label = train_dataset[idx.item()]
plt.imshow(img.squeeze())       # can input img
plt.show()
print(img.shape)
print(label)

# self[i][ ind[i][j] ] = src[i][j]
print(
    torch.zeros([3,10]).scatter_(1, torch.tensor([[7], [2], [5]]), value=1)
)

# custom dataset
class custom_dataset(Dataset):
    def __init__(self, annotation_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotation_file, names=['file_name', 'label'])
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)
    
    def __getitem__(self, idx):
        '''
            return samples corresponding to index from datasets 
        '''
