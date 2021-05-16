import heapq

list1=[34,25,12,99,87,63,58,78,88,92]
list2=[
    {'name':'IBM','shares':100,'price':91.1},
    {'name':'aapl','shares':50,'price':543.22},
    {'name':'fb','shares':200,'price':21.09},
    {'name':'hpq','shares':35,'price':31.75},
    {'name':'thoo','shares':45,'price':16.35},
    {'name':'acme','shares':75,'price':115.65}]
print(heapq.nlargest(3,list1))
print(heapq.nsmallest(3,list1))
print(heapq.nlargest(2,list2,key=lambda x:x['price']))
print(heapq.nlargest(2,list2,key=lambda x:x['shares']))
