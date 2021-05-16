import math

def fx(x):
    y=x*x*x-2*x-5
    return y

a=2
b=3
cye=0

while abs(b-a)>0.0005:
    x=(b+a)/2
    if fx(a)*fx(x)>0:
        a=x
    else:
        b=x
    cye=cye+1

print(x)
print(cye)
