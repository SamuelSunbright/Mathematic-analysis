x=eval(input("please input the initial x0 = "))
n=0

def f(x):
    return x*x*x-x-1

def fd(x):
    return 3*x*x-1

while True:
    lam=1
    y=x-lam*f(x)/fd(x)
    while abs(f(y))>abs(f(x)):
        lam=lam/2
        y=x-lam*f(x)/fd(x)
    if abs(y-x)<5E-6:
        print(y)
        print(lam)
        print(n+1)
        break
    else:
        x=y
        n=n+1
        continue


