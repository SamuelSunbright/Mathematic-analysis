def fumular1():
    x=eval(input())
    n=0
    while True:
        x1=1+1/(x*x)
        print(x1)
        if abs(x1-x)<0.5E-5:
            break
        else:
            x=x1
            n=n+1
            continue
    print('answer is {}'.format(x))
    print('cycle time is{}'.format(n))
    return 0

def fumular2():
    x=eval(input())
    n=0
    while True:
        x1=pow((1+x*x),1/3)
        print(x1)
        if abs(x1-x)<0.5E-5:
            break
        else:
            x=x1
            n=n+1
            continue
    print('answer is {}'.format(x))
    print('cycle time is{}'.format(n))
    return 0

def fumular3():
    x=eval(input())
    n=0
    while True:
        x1=pow((x-1),-0.5)
        print(x1)
        if abs(x1-x)<0.5E-5:
            break
        else:
            x=x1
            n=n+1
            continue
    print('answer is {}'.format(x))
    print('cycle time is{}'.format(n))
    return 0

def fumular4():
    x=eval(input())
    n=0
    while True:
        x1=1+1/(x*x)
        x2=1+1/(x1*x1)
        x3=x2-pow((x2-x1),2)/(x2-2*x1+x)
        print(x3)
        if abs(x3-x)<0.5E-5:
            break
        else:
            x=x3
            n=n+1
            continue
    print('answer is {}'.format(x))
    print('cycle time is{}'.format(n))
    return 0

def fumular5():
    x=eval(input())
    n=0
    while True:
        x1=pow((1+x*x),1/3)
        x2=pow((1+x1*x1),1/3)
        x3=x2-pow((x2-x1),2)/(x2-2*x1+x)
        print(x3)
        if abs(x3-x)<0.5E-5:
            break
        else:
            x=x3
            n=n+1
            continue
    print('answer is {}'.format(x))
    print('cycle time is{}'.format(n))
    return 0
    

