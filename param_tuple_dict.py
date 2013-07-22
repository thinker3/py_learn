def f(*x):
    print x

def g(**x):
    print x

def h(*x,**y):
    print x,y
f(1,2,5)
g(a='1',b='2',c='3')
h(1,2,3,a=1,b=2,c=3)
