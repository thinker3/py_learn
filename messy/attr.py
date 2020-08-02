#!/usr/bin/env python
# encoding: utf-8


class Test(object):
    name = 'python'

t = Test()
print(hasattr(t, 'name'))  # not has_attr
print(getattr(t, 'name', 'null'))  # not get_attr
