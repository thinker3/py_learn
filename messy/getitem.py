#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = {'a': 'alpha', 'b': 'beta'}
assert data.__getitem__('a') == data['a'] == 'alpha'

try:
    object.__getitem__(data, 'b')
except Exception as e:
    print e

array = ['alpha', 'beta', 'gamma']
assert array.__getitem__(0) == array[0] == 'alpha'
assert array.__getitem__(-1) == array[-1] == 'gamma'
assert array[1:] == array.__getitem__(slice(1, None))

seq = ('alpha', 'beta')
assert seq.__getitem__(0) == seq[0] == 'alpha'
assert seq.__getitem__(-1) == seq[-1] == 'beta'
