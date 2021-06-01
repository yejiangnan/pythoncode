import numpy as np

arr=np.array([[2,2,3],
             [2,5,6]],dtype=float)
print(arr)
print(arr.dtype)

arr=np.zeros((3,4))
print(arr)

arr=np.ones((4,5))
print(arr)

arr=np.empty((3,4))
print(arr)

arr=np.arange(0,10,2)
print(arr)

arr=np.arange(12).reshape((3,4))
print(arr)

arr=np.linspace(0,10,6).reshape((2,3)) #0-10 5个数，每个数距离相等
print(arr)

arr=np.random.rand(4,4)
print(arr)