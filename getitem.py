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
