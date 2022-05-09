# To compute gradients, pytorch has a built-in 
# automatic differentiatioin engine called 'torch.autograd'.
# It supports automatic calculation of gradients for all calculation graphs.

import torch
import torch.nn.functional as F


x = torch.ones(5)
y = torch.zeros(3)
w = torch.randn(5, 3, requires_grad=True)   # >> param
b = torch.randn(3)      # >> param
b.requires_grad_(True)
z = torch.matmul(x, w) + b
loss = F.binary_cross_entropy_with_logits(z, y)

# change requires_grad state 
# x.requires_grad_(True)

print(f"gradient func for z = {z.grad_fn}")
print(f"gradient func for loss = {loss.grad_fn}")

loss.backward()
print(w.grad)
print(b.grad)

# no_grad temporarily set all the requires_grad flag to false
# it will use less memory because it knows from the beginning 
# that no gradients are needed so it doesn't need to keep intermediary results
with torch.no_grad():
    z = torch.matmul(x, w) + b
print(f"torch.no_grad = {z.requires_grad}")

# detach creates a new tensor that shares storage with the tensor
# that does not require grad.
# it detaches the output from the computational graph.
z = torch.matmul(x, w) + b
print(z.requires_grad)
z_det = z.detach()
print(z.requires_grad)
print(z_det.requires_grad)
