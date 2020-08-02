#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import (
    Identity,
    Matrix,
    MatrixSymbol,
    Determinant,
)

E = Identity(3)
print(E)
print(E.as_mutable())
print(E.as_explicit())

X = MatrixSymbol('X', 3, 3)
print(X)
print(X.T)
MX = Matrix(X)
print(MX)
print(Matrix(X.I))
print(Matrix(X.T))
print(Matrix(X.T * X))

print(Determinant(X))
# assert Determinant(X) == Determinant(X.T)
DX = Determinant(MX)
print(DX)
