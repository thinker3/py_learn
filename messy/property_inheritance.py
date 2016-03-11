#!/usr/bin/env python
# encoding: utf-8


class A(object):
    name = 'John'

    @property
    def length(self):
        return len(self.name)


class B(A):
    pass


b = B()
print b.name
print b.length
