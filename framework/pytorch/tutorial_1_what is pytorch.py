# -*- encoding: utf-8 -*-
# Author: Inyong Hwang
# PyTorch tutorial 1
# Reference
# PyTorch tutorial
# https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py
# torch random seed
# https://m.blog.naver.com/atelierjpro/221175394278

import torch

# Random Seed

# CPU

print(torch.initial_seed())
torch.manual_seed(37)

'''
# GPU

print(torch.cuda.initial_seed())
torch.cuda.manual_seed_all(37
'''

# Tensors

x = torch.empty(5, 3)
print(x)

x = torch.rand(5, 3)
print(x)

x = torch.zeros(5, 3, dtype=torch.long)
print(x)

x = torch.tensor([5.5, 3])
print(x)

x = x.new_ones(5, 3, dtype=torch.double)
print(x)

x = torch.rand_like(x, dtype=torch.float)
print(x)

print(x.size())

# Operations

y = torch.rand(5, 3)
print(x + y)

print(torch.add(x, y))

result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)

y.add_(x)
print(y)

print(x[:, 1])

x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())

x = torch.randn(1)
print(x)
print(x.item())

# NumPy Bridge

a = torch.ones(5)
print(a)

b = a.numpy()
print(b)

a.add_(1)
print(a)
print(b)

# Converting NumPy Array to Torch Tensor

import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)

'''
# CUDA Tensors

# let us run this cell only if CUDA is available
# We will use ``torch.device`` objects to move tensors in and out of GPU
if torch.cuda.is_available():
    device = torch.device("cuda")          # a CUDA device object
    y = torch.ones_like(x, device=device)  # directly create a tensor on GPU
    x = x.to(device)                       # or just use strings ``.to("cuda")``
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))       # ``.to`` can also change dtype together!
'''
