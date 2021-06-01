import numpy as np

A=np.arange(3,15).reshape(3,4)
print(A) 
print(A[2])
print(A[2][1])
print(A[2,1])
print(A[2,:])
print(A[:,1])
print(A[1,1:3])
for row in A:
    print(row)
for col in A.T:
    print(col)
print(A.flatten()) #按顺序排成一行
for item in A.flat: #迭代每一个元素
    print(item)