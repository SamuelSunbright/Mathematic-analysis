import math

def fx(x,y):
    return x*math.exp(x)-y
def dfx(x):
    return (x+1)*math.exp(x)
def func(x):
    error=0.0000001
    x0=x
    alpha=x0
    while True:
        x1=x0-fx(x0,alpha)/dfx(x0)
        if abs(x1-x0)<error:
            break
        else:
            x0=x1
            continue
    return x1

x0=-1/math.exp(1)
xn=10
h=0.1
for i in range(int((xn-x0)/h)):
    y=func(x0+i*h)
    print(y)

input("press anykey to exit")
