#!/usr/bin/env python
#coding=utf-8
 
#2013年 04月 23日 星期二 16:21:13 CST

def Gen1(x, y):
		for i in xrange(x):
				for j in xrange(y):
						yield(i, j)

def Gen2(x, y):
		return ((i, j) for i in xrange(x) for j in xrange(y))

g = Gen1(2,3)
for i in g:
		print i

h = Gen2(2,3)
print
for i in h:
		print i
		
