import torch
import torchvision.models as models

model = models.vgg11(pretrained=True)

optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
optimizer2 = torch.optim.SGD([
    {"params": model.base.parameters()},
    {"params": model.classifier.parameters(),
    "lr": 1e-3}
], lr=1e-2)
