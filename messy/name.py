#!/usr/bin/env python
# -*- coding: utf-8 -*-

print __name__, type(__name__)  # __main__ <type 'str'>


if __name__ != '__main__':
    print 'being imported'
