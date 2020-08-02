#!/usr/bin/env python
# encoding: utf-8

print(__import__)

#mod = __import__('imported.py')  # ImportError: No module named py
mod = __import__('imported')
print(mod)
print(mod.s)
