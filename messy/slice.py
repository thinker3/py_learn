#!/usr/bin/env python
# -*- coding: utf-8 -*-

array = ['alpha', 'beta', 'gamma']

print(array.__getitem__(slice(1,)))
print(array.__getitem__(slice(None, 1)))
print(array.__getitem__(slice(None, None)))
print(array.__getitem__(slice(None, None, 2)))
