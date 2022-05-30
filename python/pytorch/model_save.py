from tkinter.tix import Tree
import torch
import torchvision.models as models

# torch.save(model.state_dict()) save params of model
# not model instance
model = models.vgg16(pretrained=True)
torch.save(model.state_dict(), "model_weights.pth")

model1 = models.vgg16()
model1.load_state_dict(torch.load("model_weights.pth"))
model.eval()

# Note: before inference step,
# Call model.eval() to set dropout and bn evaluation mode
# otherwise, inconsistent output will be generated.
