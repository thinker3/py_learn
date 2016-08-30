#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

sample = 'a1b2c3'

result = re.search("[a-z]\d", sample)
print result.group()  # a1 # group(0) == group()
print result.groups()  # ()
print '*' * 30

result = re.search("([a-z]\d)([a-z]\d)", sample)
print result.lastindex  # 2
print result.group()  # a1b2
print result.group(0)  # a1b2
print result.group(1)  # a1
print result.group(2)  # b2
print result.groups()  # ('a1', 'b2')
