names=['Guanyv','Zhangfei','Zhaoyun','Maochao','Huangzhong']
courses=['Chinese','Math','English']
scores=[[None]*len(courses) for _ in range(len(names))]
for row,name in enumerate(names):
    for col,course in enumerate(courses):
        scores[row][col]=float(input(f'please input {course}score of {name}:'))
        print(scores)
