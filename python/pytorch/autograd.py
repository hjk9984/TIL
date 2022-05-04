# To compute gradients, pytorch has a built-in 
# automatic differentiatioin engine called 'torch.autograd'.
# It supports automatic calculation of gradients for all calculation graphs.

import torch
import torch.nn.functional as F


x = torch.ones(5)
y = torch.zeros(3)
w = torch.randn(5, 3, requires_grad=True)   # >> param
b = torch.randn(3, requires_grad=True)      # >> param
z = torch.matmul(x, w) + b
loss = F.binary_cross_entropy_with_logits(z, y)

# change requires_grad state 
# x.requires_grad_(True)

print(f"gradient func for z = {z.grad_fn}")
print(f"gradient func for loss = {loss.grad_fn}")

loss.backward()
print(w.grad)
print(b.grad)
