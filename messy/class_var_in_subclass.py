#!/usr/bin/env python
# encoding: utf-8


class A(object):
    test = {}

A.test[1] = 1
print(A.test)


class B(A):
    pass

print(B().test)  # class variable shared by subclass
print('*' * 30)


class C(A):
    test = {}

C.test[2] = 2
print(C.test)
A.test[3] = 3
B.test[4] = 4
print(A.test)
print(B.test)
print(C.test)

print('*' * 30)
B.test = 'test'
print(A.test)  # not affected here
print(B.test)
