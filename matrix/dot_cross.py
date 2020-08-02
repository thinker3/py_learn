#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import (
    Matrix,
)

v1 = Matrix([1, 2, 3])
print(v1)
v2 = Matrix([4, 5, 6])
print(v2)
print(v1.dot(v2))
print(v1.cross(v2))
print(v2.cross(v1))
