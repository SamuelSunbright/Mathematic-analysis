import math

def fx(x):
    y=math.sin(x)+math.exp(x/2)-x*x
    return y

a=-1
b=1
cye=0

while abs(b-a)>0.000005:
    x=(b-a)/2
    if fx(a)*fx(x)>0:
        a=x
    else:
        b=x
    cye=cye+1

print(x)
print(cye)
