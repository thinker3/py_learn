from copy import deepcopy
flist = []
for i in xrange(3):
    def foo(x): print x + i
    flist.append(foo)

i=10
for f in flist:
    f(2)
    
print
flist = []

for i in xrange(3):
    def func(x): return x * func.i
    func.i=i
    flist.append(deepcopy(func))
i=10
for f in flist:
    print f(2)
    
print
flist = []

for i in xrange(3):
    j=5
    def func(x): return x * j
    flist.append(deepcopy(func))
j=10
for f in flist:
    print f(2)