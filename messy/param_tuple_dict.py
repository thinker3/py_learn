def f(*x):
    print x

def g(**x):
    print x

def h(*x,**y):
    print x,y
f(1,2,5)
g(a='1',b='2',c='3')
h(1,2,3,a=1,b=2,c=3)

# empty str list dict tuple as default param


def add_str(s=''):
    s += 'abc'
    print s

print '*' * 30
add_str()
add_str()


def append_list(l=[]):
    l.append('abc')
    print l

append_list()
append_list()

def append_dict(d={}):
    d[i] = i
    print d

i = 0
append_dict()
i += 1
append_dict()


def add_tuple(t=()):
    t += (1,)
    print t

add_tuple()
add_tuple()


def str_key(**kwargs):
    print kwargs

key = 'length'
str_key(**{key: len(key)})
