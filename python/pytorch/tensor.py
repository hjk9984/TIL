import torch
import numpy as np

# the tensor are similar to ndarray of Numpy,
# except that they can be computed with the gpu

# initialization
# data direct
tmp = [[1, 2], [3,4]]
x = torch.tensor(tmp)
print(x)

# numpy
np_tmp = np.array(tmp)
x_np = torch.from_numpy(np_tmp)
x_np2 = torch.tensor(np_tmp)
print(x_np, x_np2)

# tensor
# if not explicitly override, maintains attributes of the tensor
x_ones = torch.ones_like(x)
x_ones2 = torch.ones_like(x, dtype=torch.float)
print(x_ones, x_ones2)


# attribute
tmp = torch.rand(3, 4)
print(tmp.shape, tmp.dtype, tmp.device)

t1 = torch.cat([tmp, tmp], dim=0)
t2 = torch.cat([tmp, tmp], dim=1)
print(t1.shape, t2.shape)


# arithmetic operations
# matrix multiplication
y1 = tmp @ tmp.T
y2 = tmp.matmul(tmp.T)
print(y1)
print(y2)

# element-wise product
z1 = tmp * tmp
z2 = tmp.mul(tmp)
print(z1)
print(z2)


# inplace operation
# has sufix _
# it isnt faster than normal operation
# but less memory accesses, 
# this can lead to speed up if your task is bound by memory bandwidth
# x[...] = ...
print(tmp)
tmp.sub_(1)
print(tmp)


# in cpu tensor and ndarray share memory
tmp2 = torch.ones(3)
n = tmp2.numpy()
print(tmp2, n)
tmp2 += 1
print(tmp2, n)

n2 = np.ones(3)
tmp3 = torch.from_numpy(n2)
print(tmp3, n2)
n2 += 2
print(tmp3, n2)
