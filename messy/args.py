#!/usr/bin/env python
# encoding: utf-8


def pass_kwargs(a, b, c=True):
    print 'a = %s' % a
    print 'b = %s' % b
    print 'c = %s' % c

data = dict(
    c=3,
    b=2,
    a=1,
)
pass_kwargs(**data)

print '*' * 30
data = dict(
    b=2,
    a=1,
)
pass_kwargs(**data)
