#!/usr/bin/env python
# encoding: utf-8

from sys import argv

base = [1, 5, 10, 50, 100, 500, 1000]
letters = "I, V, X, L, C, D, M".split(', ')

d = {}
for i in range(len(base) - 1):
    d[base[i]] = letters[i]
    if i % 2 == 0:
        d[base[i] * 4] = letters[i] + letters[i + 1]
    else:
        d[base[i] * 9 / 5] = letters[i - 1] + letters[i + 1]
d[base[i + 1]] = letters[i + 1]
base_r = list(d.keys())
base_r.sort(reverse=True)

'''
print base_r
for i, j in d.iteritems():
    print i, j
'''


def to_roman(n):
    first = []
    m = n
    for i in base_r:
        while m - i >= 0:
            m -= i
            first.append(d[i])
    return ''.join(first)

f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        one = int(one)
        print(to_roman(one))
f.close()
