import numpy as np
import matplotlib.pyplot as plt
""" 
打斗次数，亲吻次数
[3, 199]    爱情片
[2, 132]
[127, 14]   动作片
[114, 3] 
 """

x=np.array([[3,199],[2,132],[5,87],[65,12],[127,14],[114,3]])
y=np.array(['爱情','爱情','爱情','动作','动作','动作'])
T=np.array([[25,100],[85,23]])

p=2
k=3

n_lp=[np.sum(np.abs(t-x)**2,axis=1)**(1/p) for t in T]
print(n_lp)
n_idx=np.argsort(n_lp,axis=1)[:,:k]
lbl=np.unique(y)
proba=np.array([[n[n==v].size/n.size for v in lbl] for n in y[n_idx]])
#y[n_idx]以n_idx矩阵的数为索引在y中获得的值组成和n_idx同样大小的矩阵
print(lbl[proba.argmax(axis=1)])
 


