import numpy as np

r=eval(input("please input matrix's row:"))
c=eval(input("please in put matrix's column:"))
a=np.zeros((r,c))
l=np.zeros((r,c))
u=np.zeros((r,c))

for i in range(r):
    for j in range(c):
        a[i][j]=eval(input("please input the value:"))
        if i==j:
            u[i][j]=1
b=[eval(input("please input the answer's matrix:"))for i in range(r)]

for i in range(r):
    l[i][0]=a[i][0]
    u[0][i]=a[0][i]/l[0][0]

for n in range(1,c):
    for i in range(n,r):
        s=0
        for k in range(n):
            s=s+l[i][k]*u[k][n]
        l[i][n]=a[i][n]-s

    for j in range(n+1,c):
        s=0
        for k in range(n):
            s=s+l[n][k]*u[k][j]
        u[n][j]=(a[n][j]-s)/l[n][n]

y=np.zeros(r)
y[0]=b[0]/l[0][0]
for i in range(1,r):
    s=0
    for j in range(i):
        s=s+l[i][j]*y[j]
    y[i]=(b[i]-s)/l[i][i]

x=np.zeros(r)
x[r-1]=y[r-1]
for i in range(r-1,0,-1):
    s=0
    for j in range(i,r):
        s=s+u[i-1][j]*x[j]
    x[i-1]=y[i-1]-s

print("matrix x is :",x)
print("matrix l is : \n",l)
print("matrix u is : \n",u)
input("press any key to exit")


    
