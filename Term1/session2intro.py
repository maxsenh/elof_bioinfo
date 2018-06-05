'''Introductory session 2'''
def f(a,b):
    mi=min(a,b)
    ma=max(a,b)
    lis=[]
    if mi%2==0:
        for i in range(mi,ma,2):
            lis.append(i)
    else:
        for i in range(mi+1,ma,2):
            lis.append(i)
    return sum(lis)

def chin(heads):

    listduck=[]
    listplaty=[]
    for ducks in range(0,heads):
        legd=(heads-ducks)*2
        listduck.append(legd)
    for platy in range(heads,0,-1):
        legp=(heads-platy)*4
        listplaty.append(legp)

    for i in range(0,heads):
        ex=listplaty[i]+listduck[i]
        if ex==94:
            x=listplaty[i]/4
            y=listduck[i]/2
            return "%d platypus and %d ducks"%(x,y)
   

def fact(a):
    s=1
    for i in range(1,a+1):
        s=s*i
    return s 

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

if __name__=="__main__":
    print(f(7,15))
    print(chin(35))
    print(fact(6))
    print(fib(12))
