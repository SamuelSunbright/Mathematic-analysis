import random as rand
a=rand.random()
N=10000000
n=0
for i in range(N-1):
    x=rand.random()
    y=rand.random()
    if x**2+y**2<1:
        n=n+1
print(4*n/N)
        
