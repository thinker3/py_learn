#!/usr/bin/env python
#coding=utf-8
#2013年 04月 23日 星期二 15:57:36 CST

import datetime
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

def my_permutations(n):
    ans = [[0]]
    if n <= 0:
        return ans
    i = 1
    temp = []
    while i < n+1:
        for one in ans:
            for j in range(i+1):
                two = one[:]
                two.insert(j, i)
                temp.append(two)
        ans = temp 
        temp = []
        i += 1
    return ans

ans = my_permutations(3)
print ans, len(ans)


def my_permutations_generator(n):
    ans = [[0]]
    if n <= 1:
        yield ans[0]
    temp = []
    for i in range(1, n):
        for one in ans:
            for j in xrange(i,-1,-1):
                two = one[:]
                two.insert(j, i)
                if i == n-1:
                    yield two
                else:
                    temp.append(two)
        ans = temp 
        temp = []

times = []
num = 7

now = datetime.datetime.now()
for one in my_permutations_generator(num):
    print one
delta = (datetime.datetime.now() - now)
times.append(delta)

print '*' * 20

def my_permutations_generator_faster(n):
    indices = range(n)
    cycles = range(n, 0, -1)
    yield indices
    while n:
        for i in reversed(range(n)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield indices
                break
        else:
            return

now = datetime.datetime.now()
for one in my_permutations_generator_faster(num):
    print one
delta = (datetime.datetime.now() - now)
times.append(delta)

for one in times:
    print one

def permute_in_place(a):
    '''
    >>> a = range(4)
    >>> a
    [0, 1, 2, 3]
    >>> a[2:]
    [2, 3]
    >>> a[2:] = [8,9,10]
    >>> a
    [0, 1, 8, 9, 10]
    '''
    yield list(a)

    if len(a) <= 1:
        return

    last = len(a)
    while 1:
        i = last - 1

        while 1:
            i = i - 1
            if a[i] < a[i+1]:
                j = last - 1
                while not (a[i] < a[j]):
                    j = j - 1
                a[i], a[j] = a[j], a[i]
                r = a[i+1:last]
                r.reverse()
                a[i+1:last] = r
                yield list(a)
                break
            if i == 0:
                a.reverse()
                return

for one in permute_in_place(range(4)):
    print one





