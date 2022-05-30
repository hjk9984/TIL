

# I guess clone is used to backup the variable like modification of the box representation.

import torch

tmp = torch.tensor([1])
print(id(tmp))
tmp = tmp + 1
print(id(tmp))
tmp[0] = 3
print(id(tmp))

# sum = 2*x + 3*x
x = torch.ones(5,requires_grad=True)
y = x**2
z = x.clone()       # if change clone to detach, it will raise error
z.zero_()

# you can use cloned var if you dont use original var
y.sum().backward()
print(x.grad)

#z = x.clone()*3
# sum = (y+z).sum()
# sum.backward()
# print(x.grad) # tensor([5., 5., 5., 5., 5.])

# print(y.grad)

