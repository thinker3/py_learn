# coding=utf8
# 测试
#l = [[1],[1],[2]]
l = [(1,), (1,), (2,)]
s = set(l)
print s

l = [1, 2, 3]
t = tuple(l)
print t

s = set()
print s
s.add(1)
s.add('a')
print s

t = tuple()
print t
# t.append(1) #no attr append, since tuples are immutable

# set union intersection difference | & -
a = set([1, 2, 3, 4])
b = set([1, 4, 7])
print a, b
print a | b
print a & b
print a - b

a = set([1, 2, 3, 4])
b = set([1, 4, 7])
c = set([2, 4])

d = [a, b, c]

print set.intersection(*d)
print set.union(*d)


def unique(seq):
    temp = []
    for x in seq:
        #if not x in temp:
        if x not in temp:
            temp.append(x)
    return temp

t = [1, 2, 2, 3, 2, 5, 1, 3, 6, 5, 2, 7]
print unique(t)


def unique(seq):
    temp = []
    seen = set()
    for x in seq:
        if x not in seen:
            temp.append(x)
            seen.add(x)
    return temp

t = [1, 2, 2, 3, 2, 5, 1, 3, 6, 5, 2, 7]
print unique(t)
