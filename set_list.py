#l = [[1],[1],[2]]
l=[(1,), (1,), (2,)]
s = set(l)
print s

l=[1,2,3]
t=tuple(l)
print t

s=set()
print s

t=tuple()
print t
t.append(1) #no attr append
print t