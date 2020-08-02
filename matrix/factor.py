#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import (
    Matrix,
)

# A = QR of an orthogonal matrix Q and an upper triangular matrix R
A = Matrix([[1,1,1],[1,1,3],[2,3,4]])
Q, R = A.QRdecomposition()
print(R)
print(Q * Q.transpose())
print(Q * Q.T)
print(A)
print(Q * R)

# LU decomposition of a matrix is the factorization of a given square matrix into two triangular matrices, one upper triangular matrix and one lower triangular matrix
L, U, _ = A.LUdecomposition()
print(L)
print(U)
