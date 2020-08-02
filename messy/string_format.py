#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.decorators import isolate
import math


@isolate
def test():
    name = 'Jim'
    print('hello %s' % name)

    # named parameters string
    print('hello %(name)s' % {'name': name})
    print('hello %(name)s' % dict(name=name))


test()


@isolate
def format():
    # ## PEP 3101 -- Advanced String Formatting
    name = 'Tom'
    messages = 4
    print('Hello {0}, you have {1} messages'.format(name, messages))
    print('Hello {name}, you have {messages} messages'.format(name=name, messages=messages))
    print('{0:>10}, {1:>10}'.format('Hello', 123456789))
    print('{0:>10}, {1:>10}'.format('Hi', 123))
    print('{0:<10}, {1:<10}'.format('Hello', 123456789))
    print('{0:<10}, {1:<10}'.format('Hi', 123))
    print('{0:^10}, {1:^10}'.format('Hello', 123456789))
    print('{0:^10}, {1:^10}'.format('Hi', 123))

    # ## one-character placeholder
    print('{0:#^10}, {1:*^10}'.format('Hello', 123456789))
    print('{0:-^10}, {1:+^10}'.format('Hi', 123))

    print('{:.6f}'.format(math.pi))
    print('{:0.6f}'.format(math.pi))
    print('{:b}'.format(12))
    print('{:d}'.format(12))
    print('{:o}'.format(12))
    print('{:x}'.format(12))
    print('{:,}'.format(1234567890))


format()
