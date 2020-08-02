#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import (
    Matrix,
)

L = Matrix([[0, 3], [0, 7], [1, 5]])
M = Matrix([[1, 3], [-2, 3]])
N = Matrix([[0, 3], [0, 7]])


def inverse(Mat):
    a, b = Mat.shape
    if a == b:
        if Mat.det() != 0:
            return Mat ** -1


print(inverse(L))
print(inverse(M))
print(inverse(N))
print(M.inv())
print(M.inverse_LU())
print(M.inverse_GE())
print(M.inverse_ADJ())
