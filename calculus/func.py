#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import (
    symbols,
    limit,
    sqrt,
    simplify,
)

x, y = symbols('x y')
f = sqrt(x**2 + y**2)
assert limit(limit(f, x, 1), y, 2) == sqrt(5)
assert f.subs(x, 1).subs(y, 2) == sqrt(5)
assert f.subs([(x, 1), (y, 2)]) == sqrt(5)
assert f.subs({x: 1, y: 2}) == sqrt(5)

g = 's * s + 2 * s + 1'
g = simplify(g)
print(g)
assert g.subs('s', 2) == 9
assert g.subs([('s', 1)]) == 4
assert g.subs({'s': 0}) == 1


def h(x, y):
    return sqrt(x**2 + y**2)


assert h(1, 2) == sqrt(5)
assert h(4, 3) == 5
