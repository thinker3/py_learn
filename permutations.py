#!/usr/bin/env python
#coding=utf-8
#2013年 04月 23日 星期二 15:57:36 CST

import itertools
l = range(5)
t = itertools.permutations(l)
s=0
for i in t:
    print i
    s+=1
print s

s=0
for one in itertools.combinations(l, 3):
    print one
    s+=1
print s

print '*' * 20
more = ['a', 'b', 'c', 'd', 'e']
less = [1, 2, 3]
s=0
for one in itertools.combinations(more, len(less)):
    for two in itertools.permutations(one):
        for a, b in zip(two, less):
            print a, b
        print
        s+=1
print s
