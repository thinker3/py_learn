#!/usr/bin/env python
# encoding: utf-8

import ctypes

s = "Hello, World"
p = ctypes.c_char_p(s)
up = ctypes.c_wchar_p(s)
print p
print up
print p.value
print up.value
print type(p.value)
print type(up.value)
p.value = "Hi, there"
print p
print p.value
