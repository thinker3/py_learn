#!/usr/bin/env python
# encoding: utf-8

import functools
import operator


def add(a, b):
    print a + b

add_1 = functools.partial(add, 1)
add_1(5)


def say_hello(name, default="Good morning"):
    print "Hello %s, %s!" % (name, default)

say_hello('Ken')
welcome = functools.partial(say_hello, default='Welcome')
welcome('Ken')
welcome_jerry = functools.partial(welcome, 'Jerry')
welcome_jerry()


def run_callback(callback):
    callback()

run_callback(welcome_jerry)
#run_callback(welcome)  # TypeError
run_callback(functools.partial(welcome, 'Benny'))
run_callback(functools.partial(say_hello, 'Benny', 'Nice to meet you'))


def add(n):
    print functools.reduce(lambda x, y: x + y, xrange(n + 1))
    print functools.reduce(lambda x, y: x + y, xrange(n + 1), 0)
    print functools.reduce(lambda x, y: x + y, xrange(n + 1), 1)
    # TypeError: reduce() of empty sequence with no initial value
    #print functools.reduce(lambda x, y: x + y, [])
    print functools.reduce(lambda x, y: x + y, [], 0)
    print functools.reduce(lambda x, y: x + y, [], 1)
    print functools.reduce(operator.add, xrange(n + 1))


def multiply(n):
    print functools.reduce(lambda x, y: x * y, xrange(1, n + 1))
    print functools.reduce(lambda x, y: x * y, xrange(1, n + 1), 0)
    print functools.reduce(lambda x, y: x * y, xrange(1, n + 1), 1)
    #print functools.reduce(lambda x, y: x * y, [])
    print functools.reduce(lambda x, y: x * y, [], 0)
    print functools.reduce(lambda x, y: x * y, [], 1)
    print functools.reduce(operator.mul, xrange(1, n + 1))

add(100)
print '*' * 20
multiply(4)
