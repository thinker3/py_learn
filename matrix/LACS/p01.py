#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import (
    Matrix,
)

M = Matrix([[40, 15, 100], [-50, 25, 50]])
M.row_op(0, lambda v, j: v / 40)
M.row_op(1, lambda v, j: v / 50)
M.row_op(1, lambda v, j: v + M[0, j])
M.row_op(1, lambda v, j: v * 8 / 7)
M.row_op(0, lambda v, j: v + M[1, j] * (-3) / 8)
print(M)

M = Matrix([[40, 15, 100], [-50, 25, 50]])
M.zip_row_op(1, 0, lambda v, u: v + u / 40 * 50)
M.zip_row_op(0, 0, lambda v, u: v / 40)
M.zip_row_op(1, 1, lambda v, u: v / 175 * 4)
M.zip_row_op(0, 1, lambda v, u: v + u / 8 * (-3))
print(M)
