d = {'a': 'alpha', 'b': 'beta'}
print d.__getitem__('a')
print d['b']
try:
    print object.__getitem__(d, 'a')
except:
    pass

try:
    print getattr(d, 'a')
except:
    pass

try:
    print object.__getattribute__(d, 'a')
except:
    pass


print '-' * 30
l = ['alpha', 'beta', 'gamma']
print l.__getitem__(0)
print l.__getitem__(-1)
print l[1]
print l[1:]
print l.__getitem__(slice(1,None))
print l.__getitem__(slice(1,))
print l.__getitem__(slice(None,1))
print l.__getitem__(slice(None,None))
print l.__getitem__(slice(None,None,2))


print '-' * 30
t = ('alpha', 'beta')
print t.__getitem__(0)
print t.__getitem__(-1)
print t[1]
