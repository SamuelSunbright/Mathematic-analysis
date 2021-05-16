import math
import numpy

def f(x,y):
    return y-2*x/y

a=0
b=1
x=0
h=0.1
y=numpy.zeros(int((b-a)/h)+1)
y[0]=1
for i in range(4):
    k1=f(x,y[i])
    k2=f(x+h/2,y[i]+h*k1/2)
    k3=f(x+h/2,y[i]+h*k2/2)
    k4=f(x+h,y[i]+h*k3)
    y[i+1]=y[i]+h*(k1+2*k2+2*k3+k4)/6
    x=x+h
    
for i in range(4,int((b-a)/h),1):
    y[i+1]=y[i]+h*(55*f(x,y[i])-59*f(x-h,y[i-1])+37*f(x-2*h,y[i-2])-9*f(x-3*h,y[i-3]))/24
    x=x+h
print(y)
input("press any key to exit") 
