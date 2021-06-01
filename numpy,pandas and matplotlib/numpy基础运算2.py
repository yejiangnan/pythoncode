import numpy as np

""" A=np.arange(2,14).reshape((3,4))
print(A)
print(np.argmin(A)) #最小的数的位置
print(np.argmax(A)) #最大的数的位置
print(np.mean(A))
print(A.mean())
print(np.median(A))
print(np.cumsum(A))
print(np.diff(A)) #累差，每两个数差多少
print(np.nonzero(A)) #第i行j列的数是非0的，用两个向量表示行和列
print(np.sort(A)) #逐行排序
print(np.transpose(A)) #矩阵转置
print(A.T) #矩阵转置
print(A.T.dot(A))
print(np.clip(A,5,9)) #小于5的数变为5，大于9的数变为9，其余不变
print(np.mean(A,axis=0))
print(np.mean(A,axis=1)) """

#按第一列排序
data = np.array([[1,2,7],[5,3,2],[4,6,3],[7,5,1],[9,0,9]])
data = data[np.argsort(data[:,0 ])]
print(data)
