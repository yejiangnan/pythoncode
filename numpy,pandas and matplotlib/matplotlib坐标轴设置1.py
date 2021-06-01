import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure(figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.xlim((-1,2))
plt.ylim((-1,3))
plt.xlabel('I am X')
plt.ylabel('I am Y')
new_ticks=np.linspace(-1,2,50)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],['$really\ bad$','$bad$','$normal$',
                                '$good$','$really\ good$'])

plt.show()