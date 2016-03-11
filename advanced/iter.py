#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Iter(object):
    def __init__(self, children):
        self.children = children

    def add(self, *items):
        self.children.extend(items)
        return self

    def __iter__(self):
        for child in self.children:
            yield child

    def __str__(self):
        return '%s' % self.children

    def __repr__(self):
        return 'Iter(%s)' % self.children


it = Iter(range(1, 5))
for one in it.add(*range(8, 12)):
    print one
