#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

sample = 'a1b2c3'
space_sample = ' %s' % sample

result = re.search("[a-z]\d", sample)
print result.group()  # a1

result = re.search("[a-z]\d", space_sample)
print result.group()  # a1
print '*' * 30

result = re.match("[a-z]\d", sample)
print result.group()  # a1

result = re.match("[a-z]\d", space_sample)
print result  # None
print '*' * 30

result = re.findall("[a-z]\d", sample)
# type(result) <type 'list'>
print result  # ['a1', 'b2', 'c3']

result = re.findall("[a-z]\d", space_sample)
print result  # ['a1', 'b2', 'c3']
