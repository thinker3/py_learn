#!/usr/bin/env python
#coding=utf-8
#2013年 04月 23日 星期二 15:57:36 CST

import itertools
l = range(5)
t = itertools.permutations(l)
s=0
for i in t:
		print i
		s+=1
print s
