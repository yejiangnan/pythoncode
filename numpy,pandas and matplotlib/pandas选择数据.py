import pandas as pd
import numpy as np

dates=pd.date_range("20160101",periods=6)
df=pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['a','b','c','d'])
print(df)
# print(df['a'])
# print(df.a)
# print(df[0:3])
# print(df['20160101':'20160104'])

# print(df.loc['20160101'])
# print(df.loc[:,['a','b']])
# print(df.loc['20160101':'20160104',['a','b']])

# print(df.iloc[3])
# print(df.iloc[3:5,1:3])
# print(df.iloc[[1,3,5],1:3])

print(df[df.a>8])