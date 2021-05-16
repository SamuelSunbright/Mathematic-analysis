import math

def fx(x):
    if x==0:
        y=1
    else:
        y=math.atan(x)/x
    return y

a=0
b=1
n=1
h=(b-a)/2
r=0.5*(b-a)*(fx(a)+fx(b))
while True:
    s=0
    for i in range(n):
        s=s+fx(a+(2*i+1)*h)
    r1=r/2+h*s
    print(r1)
    if r1-r<0.5e-7:
        break
    else:
        r=r1
        n=2*n
        h=h/2

    
    
