import numpy as np
import matplotlib.pyplot as plt

x=np.array([19,25,31,38,44])*np.array([19,25,31,38,44])
y=np.array([19,32.3,49,73.3,97.8])

b=(sum(x)*sum(y)-len(x)*sum(x*y))/(sum(x)*sum(x)-len(x)*sum(x*x))
a=sum(y)/len(x)-b*sum(x)/len(x)

print(a,b)
x1=np.linspace(18,50,100)
y1=a+b*x1*x1
plt.plot(x1,y1)
plt.plot([19,25,31,38,44],[19,32.3,49,73.3,97.8],'ro')
plt.show()
