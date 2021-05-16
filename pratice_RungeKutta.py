import math

def f(x,y):
    return y-2*x/y

a=0
b=1
x=0
y=1
h=eval(input("please input h:"))
for i in range(int((b-a)/h)):
    k1=f(x,y)
    k2=f(x+h/2,y+h*k1/2)
    k3=f(x+h/2,y+h*k2/2)
    k4=f(x+h,y+h*k3)
    y1=y+h*(k1+2*k2+2*k3+k4)/6
    y=y1
    x=x+h
    print("y is {:.4f} when x is {:.1f}".format(y1,x))

input("press any key to exit") 
