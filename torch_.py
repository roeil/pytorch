# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:07:17 2020

@author: roy
"""

import torch

a=torch.tensor([0,1,2,3,4])
a.dtype

a.type()

a=torch.FloatTensor([0,1,2,3,4])

a.type()

a=a.type(torch.FloatTensor) #convert type

a.ndimension()
a.mean()
a-col=a.view(5,1)


a-col=a.view(-1,1)

#convert to numpy array:
np_arr=np.array([1,2,3,4])
torch_tensor=torch.from_numpy(np_arr)


convert panda to torch array

pd_series=pd.Series([2,3,0.6])
pd_to_torch=torch.from_numpy(pd_series.values)

#product and dot product
u=torch.tensor([1,2])
v=torch.tensor([3,2])

z=u*v
z=torch.dot(u,v)
torch.linspace(-2,2,steps=5)

#plot

x=torch.linspace(0,2*np.pi,100)
y=torch.sin(x)

import matplotlib.pyplot as plt

%matplotlib inline

plt.plot(x.numpy(),y.numpy())


#in 2 D


a=[[1,2,3],[5,1,4.4],[7,0.9,3]]

A=torch.tensor(a)

A[1:3,2]

a=torch.tensor([[0,1,1],[1,0,1]])
b=torch.tensor([[1,1],[1,1],[-1,1]])

c=torch.mm(A,B)

x=torch.tensor(2,requires_grad=True)
y=x**2
y.backward()
x.grad

z=x**2+2*x+1
z.backward() #calcs the derivative of z with respect to x
#when x = 2

x.grad #gives access to value of the derivative when x = 2
x.grad.zero_() #https://stackoverflow.com/questions/48001598/why-do-we-need-to-call-zero-grad-in-pytorch


#double derivative
u=torch,tensor(1,requires_grad=True)
v=torch.tensor(2,requires_grad=True)
f=u*v+u**2
f.backward() #differentiate the graph w/respect to the two points

u.grad #partia derivative of u at the two points
v.grad

#derivative of y=x**2 with values from -10 to 10
x=torch.linspace(-10,10,10,requires_grad=True)
Y=x**2
y=tirch.sum(x**2)
y.backward()
plt.plot(x.detach().numpy(),Y.detach().numpy(),label='function')

plt.plot(x.detach().numpy(),x.grad.detach().numpy(),label='derivative')


import torch.nn.functional as F
x=torch.linspace(-3,3,100,requires_grad=True)
Y=F.relu(x)
y=torch.sum(F.relu(x))
y.backward()

