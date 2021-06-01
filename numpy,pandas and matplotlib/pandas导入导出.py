import pandas as pd
import numpy as np

data=pd.read_excel("test.xlsx")
print(data)

data.to_pickle("student.pickle")

df=pd.read_pickle("student.pickle")
print(df)