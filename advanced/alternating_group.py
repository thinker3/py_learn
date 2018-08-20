#!/usr/bin/env python
# -*- coding: utf-8 -*-


def dot(a, b):
    b = list(b)
    c = [None for i in b]
    for i, e in enumerate(a):
        c[b.index(i + 1)] = e
    return tuple(c)

even = [
    (1, 2, 3, 4),
    (1, 3, 4, 2),
    (1, 4, 2, 3),
    (2, 1, 4, 3),
    (2, 3, 1, 4),
    (2, 4, 3, 1),
    (3, 1, 2, 4),
    (3, 2, 4, 1),
    (3, 4, 1, 2),
    (4, 1, 3, 2),
    (4, 2, 1, 3),
    (4, 3, 2, 1),
]
g01 = (1, 2, 3, 4)
g02 = (1, 3, 4, 2)
g03 = (1, 4, 2, 3)
g04 = (2, 1, 4, 3)
g05 = (2, 3, 1, 4)
g06 = (2, 4, 3, 1)
g07 = (3, 1, 2, 4)
g08 = (3, 2, 4, 1)
g09 = (3, 4, 1, 2)
g10 = (4, 1, 3, 2)
g11 = (4, 2, 1, 3)
g12 = (4, 3, 2, 1)

assert dot(g01, g01) == g01
assert dot(g04, g04) == g01
assert dot(g09, g09) == g01
assert dot(g12, g12) == g01

assert dot(g02, g02) == g03
assert dot(g03, g03) == g02
assert dot(g02, g03) == g01

assert dot(g05, g05) == g07
assert dot(g07, g07) == g05
assert dot(g05, g07) == g01

assert dot(g06, g06) == g10
assert dot(g10, g10) == g06
assert dot(g06, g10) == g01

assert dot(g08, g08) == g11
assert dot(g11, g11) == g08
assert dot(g08, g11) == g01

# non-abelian, non-commutative
assert dot(g02, g04) == g07
assert dot(g04, g02) == g06

assert dot(g03, g04) == g10
assert dot(g04, g03) == g05

assert dot(g02, g05) == g09
assert dot(g03, g05) == g11
assert dot(g04, g05) == g03


matrix = []
for i in range(12):
    row = []
    for j in range(12):
        r = dot(even[i], even[j])
        index = even.index(r)
        row.append('{0:>2}'.format(index + 1))
    matrix.append(row)
for one in matrix:
    print(one)
