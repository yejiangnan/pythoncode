import numpy as np
from numpy.lib.index_tricks import AxisConcatenator

A=np.array([1,1,1])
B=np.array([2,2,2])

C=np.vstack((A,B)) #vertical stack 向下合并
D=np.hstack((A,B)) #horizontal stack 左右合并
print(A)
print(B)
print(C)
print(A.shape,C.shape)
print(D)
print(A.shape,D.shape)

""" print(A[np.newaxis,:].shape) #在行上加了一个维度
print(A[:,np.newaxis].shape) #在列上加了一个维度
print(A[:,np.newaxis])
A=A[:,np.newaxis]
B=B[:,np.newaxis]
print(np.hstack((A,B)))
print("\n")
C=np.concatenate((A,B,B,A),axis=0)
print(C)
C=np.concatenate((A,B,B,A),axis=1)
print(C)
 """
