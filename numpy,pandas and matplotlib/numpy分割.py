import numpy as np

A=np.arange(12).reshape((3,4))
print(A)
print(np.split(A,2,axis=1))
print(np.split(A,3,axis=0))
print(np.array_split(A,3,axis=1)) #在行方向做不等份分割
print(np.vsplit(A,3))
print(np.hsplit(A,2))