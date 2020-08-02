#!/usr/bin/env python
# -*- coding: utf-8 -*-

# reduced row echelon form

from sympy import (
    Matrix,
)

A = Matrix([
    [1, 0, 1, 3],
    [2, 3, 4, 7],
    [1, 3, 3, 4],
])
print(A.rref())

B = Matrix([
    [40, 15, 100],
    [-50, 25, 50],
])
print(B.rref())

C = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
print(C.rref())

D = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
])
print(D.rref())
