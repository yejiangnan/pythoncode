import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from numpy.core.fromnumeric import shape
from numpy.core.shape_base import hstack

class node:
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right
        self.v=0

class kdtree(node):
    def __init__(self,data,res):
        self.root=node(data,None,None)
        self.x=data
        self.y=res
        self.dim=data[0].size
    
    def kdtreeinit(self,u,idx=0):
        if u.data.shape[0]<=1:
            return
        u.data=u.data[np.argsort(u.data[:,idx])]
        mid=(0+u.data.shape[0])//2
        ldata=np.array([u.data[i] for i in range(0,mid)])
        rdata=np.array([u.data[i] for i in range(mid+1,u.data.shape[0])])
        u.data=np.array([u.data[mid]])
        u.left=node(ldata,None,None)
        u.right=node(rdata,None,None)
        self.kdtreeinit(u.left,(idx+1)%self.dim)
        self.kdtreeinit(u.right,(idx+1)%self.dim)
    
    def knn_predict(self,k,x):
        res=self.get_knn(k,x)
        n_lp=np.zeros((k,self.dim))
        proba=[]
        for i in range(len(res)):
            for j in range(len(res[0])-1):
                n_lp[i][j]=res[i][j]
        for i in range(len(n_lp)):
            for j in range(len(self.x)):
                if (n_lp[i]==self.x[j]).all():
                    proba.append(self.y[j])
        value=Counter(proba).most_common()
        return value[0][0]    
    
    def get_knn(self,k,x):
        L=np.zeros((k,self.dim+1))
        for i in L:
            i[self.dim]=np.inf
        self.clear(self.root)
        self.search(self.root,L,x,0,k)
        return L
    
    def clear(self,u):
        u.v=0
        if u.left!=None: self.clear(u.left)
        if u.right!=None: self.clear(u.right)
    
    def search(self,u,L,x,idx,k):
        if u.v==1 or u.data.shape[0]==0: return
        if u.left!=None and u.right!=None:
            p=x[idx]
            r=u.data[0][idx]
            if p<=r: self.search(u.left,L,x,(idx+1)%self.dim,k)
            else: self.search(u.right,L,x,(idx+1)%self.dim,k)
        # leafnode 
        else:
            u.v=1
            t1=np.array([i for i in u.data[0]])
            t2=float(np.sum(np.abs(x-u.data)**2,axis=1)**0.5)
            t1=np.hstack((t1,np.array([t2])))
            for i in L:
                if i[self.dim]>t2:
                     for j in range(len(i)):
                         i[j]=t1[j]
                     break
            t3=np.array(L[np.argsort(-L[:,self.dim ])])
            for i in range(len(t3)):
                for j in range(len(t3[0])):
                    L[i][j]=t3[i][j]
            return
        # backtrack from children
        if u.v==0:
            u.v=1
            t1=np.array([i for i in u.data[0]])
            t2=float(np.sum(np.abs(x-u.data)**2,axis=1)**0.5)
            t1=np.hstack((t1,np.array([t2])))
            for i in L:
                if i[self.dim]>t2:
                    for j in range(len(i)):
                        i[j]=t1[j]
                    break
            dist=np.abs(x[idx]-u.data[0][idx])
            t3=np.array(L[np.argsort(-L[:,self.dim ])])
            for i in range(len(t3)):
                for j in range(len(t3[0])):
                    L[i][j]=t3[i][j]
            for i in L:
                if i[self.dim]>dist:
                    self.search(u.left,L,x,(idx+1)%self.dim,k)
                    self.search(u.right,L,x,(idx+1)%self.dim,k)
                    break
            
            
# k=3            
# x=np.array([[3,199],[2,132],[5,87],[65,12],[127,14],[114,3]])
# y=np.array(['爱情','爱情','爱情','动作','动作','动作'])
# test=np.array([[25,100],[85,23]])  
# T=kdtree(x,y)
# T.kdtreeinit(T.root)
# for i in test:
#     T.knn_predict(3,i)