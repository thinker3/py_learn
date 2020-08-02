#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import (
    Matrix,
)

A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
B1 = Matrix([
    [11],
    [12],
    [13],
])
B2 = Matrix([
    [14],
    [15],
    [16],
])
B3 = Matrix([
    [17],
    [18],
    [19],
])
B = B1.row_join(B2).row_join(B3)
print(B)
C = A * B
print(C)
D = (A * B1).row_join(A * B2).row_join(A * B3)
print(D)
assert C == D
