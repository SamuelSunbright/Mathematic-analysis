import numpy as np
import math
import matplotlib.pyplot as plt

x=np.array([-1/5,-1/10,-1/15,-1/20,-1/25,-1/30,-1/35,-1/40,-1/50,-1/60,-1/70])
y=np.array([math.log(1e-4*1.27),math.log(1e-4*2.16),math.log(1e-4*2.86),math.log(1e-4*3.44),math.log(1e-4*3.87),math.log(1e-4*4.15),math.log(1e-4*4.37),math.log(1e-4*4.51),math.log(1e-4*4.62),math.log(1e-4*4.65),math.log(1e-4*4.66)])

b=(sum(x)*sum(y)-len(x)*sum(x*y))/(sum(x)*sum(x)-len(x)*sum(x*x))
a=sum(y)/len(x)-b*sum(x)/len(x)

print(a,b)
x1=np.linspace(1,80,100)
y1=math.exp(a)*np.exp(-b/x1)
y2=np.array([0,1.27,2.16,2.86,3.44,3.87,4.15,4.37,4.51,4.62,4.65,4.66])
plt.plot(x1,y1)
plt.plot([0,5,10,15,20,25,30,35,40,50,60,70],1e-4*y2,'ro')
plt.show()
