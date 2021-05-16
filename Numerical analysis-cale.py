n=2
a=2
while True:
    s=1
    b=a
    for i in range(n):
        s=s*(i+1)
    a=a+1/s
    n=n+1
    if abs(b-a)<0.5E-6:
        break
    else:
        continue
print(a)
    
    
