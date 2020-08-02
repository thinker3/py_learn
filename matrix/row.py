#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import (
    ones,
    Matrix,
)


def f(i, j):
    if i == j:
        return 1
    else:
        return 0


A = ones(3)
print(A)
print(A.rank())
B = A.elementary_row_op(row=0, k=2)
print(B)
B.row_swap(0, 1)
print(B)
C = B.elementary_row_op('n->n+km', k=3, row1=2, row2=0)
print(C)

E = Matrix(4, 4, f)
print(E)
print(E.rank())
print(E.row(0))
print(E.row(2))
