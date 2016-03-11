#!/usr/bin/env python
# encoding: utf-8


def make_adder_and_setter(x):
    x = x
    def setter(n):
        x = n # defining
    return (lambda y: x + y, setter)

adder, setter = make_adder_and_setter(10)
print adder(5)
setter(1)
print adder(5)


print '-' * 30
def make_adder_and_setter(x):
    x = [x]
    def setter(n):
        x[0] = n # not defining, but using
    return (lambda y: x[0] + y, setter)

adder, setter = make_adder_and_setter(10)
print adder(5)
setter(1)
print adder(5)


print '-' * 30
def test():
    for i in range(3):
        def a():
            print i
            print locals()
        a()
        yield a
    print locals()

a, b, c = test()
print '-' * 30
a()
b()
c()


print '-' * 30
def test():
    def func(i):
            def a():
                print i
            return a
    for i in range(3):
        yield func(i)

a, b, c = test()
a()
b()
c()
