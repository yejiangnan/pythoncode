import numpy as np

a=np.arange(4)
b=a
c=a
d=b
print(id(a))
print(id(b))
print(id(c))
print(id(d))
a[0]=11
d[1:3]=[22,33]
print(a)
print(b)
print(c)
print(d)

b=a.copy() # deep copy
print(id(a),id(b))