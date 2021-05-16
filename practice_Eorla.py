import math

def f(x,y):
    return y-2*x/y

a=0
b=1

def method1(h,x,y):
    global a,b
    for i in range(int((b-a)/h)):   
        y1=y+h*f(x,y)
        y=y1
        x=x+h
    return print(y)

def method2(h,x,y):
    global a,b
    for i in range(int((b-a)/h)):   
        y1=y+h*f(x,y)
        y2=y+h*f(x+h,y1)
        y=y2
        x=x+h
    return print(y)    

def method3(h,x,y):
    global a,b
    for i in range(int((b-a)/h)):   
        y1=y+h*f(x,y)
        y2=y+0.5*h*(f(x,y)+f(x+h,y1))
        y=y2
        x=x+h
    return print(y)   

