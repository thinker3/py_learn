#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

a = u'不要家私的勿扰'
aa = u'不需要家私的勿扰'
aaa = u'不要家私者勿扰'
aaaa = u'不需要家私者勿扰'
p = ur'不需?要家私[的者]勿扰'
b = re.search(p, a, re.I).group()
c = re.search(p, aa, re.I).group()
d = re.search(p, aaa, re.I).group()
e = re.search(p, aaaa, re.I).group()
print b, c, d, e

print
s = '毛织物 Woollen fabrics shrink in the wash. 缩水。a test'
p = re.compile(r'\w+')  # english only
word_list = p.findall(s)
print word_list
word_list = filter(lambda x: len(x) > 2, word_list)
print word_list

p = re.compile(r'\w{2,}')  # english only
word_list = p.findall(s)
print word_list

pattern = re.compile(ur'^[\u4e00-\u9fa5][A-Za-z][A-Za-z0-9]{5}$')
truck_num = u'渝A12345'
print pattern.match(truck_num)
print pattern.match('渝A12345')
print pattern.match(u'渝A1234')
print pattern.match(u'渝A123456')
