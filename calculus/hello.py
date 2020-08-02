#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://docs.sympy.org/latest/tutorial/calculus.html

from sympy import (
    init_printing,
    symbols,
    limit,
    oo,
    exp,
    cos,
    sin,
    diff,
    integrate,
    Derivative,
    Integral,
)

init_printing(use_unicode=True)

assert 10**10 < oo

x, y = symbols('x, y')
f = Integral(x**2, x)
print(f)
assert f.doit() == x**3 / 3

assert limit(x**2, x, 2) == 4

print(sin(1) / cos(1))
print(exp(x))

assert integrate(x, (x, 0, 2)) == 2
z = Integral(x**2, (x, 0, 2))
print(z)
assert z.doit() == 8 / 3

assert diff(x**2, x) == 2 * x
assert diff(x**3, x, 2) == 6 * x

assert diff(x * y, x) == y
z = Derivative((x**2) * y, x)
print(z)
assert z.doit() == 2 * x * y


if __name__ == '__main__':
    pass
