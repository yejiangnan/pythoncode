import numpy as np

a=np.array([10,20,30,40])
b=np.arange(4)
print(a,b)
c=a-b
print(c)
c=b**2
print(c)
c=10*np.sin(a) #对a的每一个值求sin再乘10
print(c)
print(b<3)

a=np.array([[1,1],
            [0,1]])
b=np.arange(4).reshape((2,2))
c=a*b   #对应位置逐个相乘
c_dot=np.dot(a,b) #矩阵乘法
c_dot2=a.dot(b)  #矩阵a乘b
print(c)
print(c_dot)
print(c_dot2)

a=np.random.random((2,4))
print(a)
print(np.sum(a,axis=1))
print(np.max(a,axis=0))
print(np.min(a,axis=1)) # axis=1在每行操作，axis=0在每列操作