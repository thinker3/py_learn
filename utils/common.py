#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DictObject(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def update(self, **kwargs):
        self.__dict__.update(kwargs)


if __name__ == '__main__':
    do = DictObject(a=1, b=2)
    print do.a, do.b
    do.update(c=3)
    print do.a, do.b, do.c
