import pandas as pd
import numpy as np

dates=pd.date_range("20160101",periods=6)
df=pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['a','b','c','d'])
print(df)
df.iloc[2,2]=1111
df.loc['20160101','b']=2222
print(df)
df.a[df.a>4]=0
print(df)
df['e']=np.nan
print(df)
df['f']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20160101',periods=6))
print(df)