from numpy.core.arrayprint import IntegerFormat
from numpy.core.numeric import outer
import pandas as pd
import numpy as np

df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])

res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res)

df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
print(df1)
print(df2)
print("\n")
res=pd.concat([df1,df2],join="inner",ignore_index=True) #join={"outer","inner"}
#默认为outer，outer把两者作并，inner把两者作交
print(res)

res=pd.concat([df1,df2],axis=1)
print(res)
res=pd.concat([df1,df2.reindex_like(df1)],axis=1) 
#把df2在df1中有坐标的加入，其他舍去，没有的项用nan填充
print(res)

df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
res=df1.append(df2,ignore_index=True)
print(res)
res=df1.append([df2,df2],ignore_index=True)
print(res)
s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
res=df1.append(s1,ignore_index=True)
print(res)