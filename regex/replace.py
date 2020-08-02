#!/usr/bin/env python
# encoding: utf-8


import re

s = "([({}))[[]{}]{}"
s = re.sub('\(\)|\[\]|{}', '', s)
print(s)
