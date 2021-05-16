import numpy as np
import math
import matplotlib.pyplot as plt

x=np.array([1,1/2,1/3,1/4,1/5,1/6,1/7,1/8])
y=np.array([1/4,1/6.4,1/8,1/8.8,1/9.22,1/9.5,1/9.7,1/9.86])

b=(sum(x)*sum(y)-len(x)*sum(x*y))/(sum(x)*sum(x)-len(x)*sum(x*x))
a=sum(y)/len(x)-b*sum(x)/len(x)

print(a,b)
x1=np.linspace(0.5,9,100)
y1=1/(a+b/x1)
plt.plot(x1,y1)
plt.plot([1,2,3,4,5,6,7,8],[4,6.4,8,8.8,9.22,9.50,9.70,9.86],'ro')
plt.show()
