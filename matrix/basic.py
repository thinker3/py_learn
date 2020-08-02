#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import (
    diag,
    Matrix,
)

M = diag(1, 2, 3)
print(M)
M = Matrix([[3, -2,  4, -2], [5,  3, -3, -2], [5, -2,  2, -2], [5, -2, -3,  3]])
print(M.det())
print(M.eigenvals())
print(M.eigenvects())
P, D = M.diagonalize()
print(D)
assert P * D * P.inv() == M
