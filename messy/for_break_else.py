#!/usr/bin/env python
# encoding: utf-8

for i in range(10):
    if i == 20:
        print i
        break
else:
    print 'else'


for i in range(10):
    if i == 2:
        print 'break'
        break
else:
    print 'else'
