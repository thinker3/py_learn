#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A(object):
    # class variables are not shared among processes
    numbers = []

    def append(self, num):
        self.numbers.append(num)


a = A()
a.append(1)
print(a.numbers)
b = A()
print(b.numbers)
