#l = [[1],[1],[2]]
l=[(1,), (1,), (2,)]
s = set(l)
print s

l=[1,2,3]
t=tuple(l)
print t

s=set()
print s
s.add(1)
s.add('a')
print s

t=tuple()
print t
# t.append(1) #no attr append, since tuples are immutable

# set union intersection difference | & -
a = set([1, 2, 3, 4])
b = set([1, 4, 7])
print a, b
print a|b
print a&b
print a-b




