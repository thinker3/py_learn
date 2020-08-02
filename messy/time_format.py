#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime as dt

now = dt.datetime.now()
time = now.time()
print(time.strftime('%H:%M'))
print(time.strftime('%H:%M:%S'))

time_string = '20:13:14'
# AttributeError: type object 'datetime.time' has no attribute 'strptime'
# print dt.time.strptime(time_string, '%H:%M')
# print dt.time.strptime(time_string, '%H:%M:%S')

# ValueError: unconverted data remains: :14
# print dt.datetime.strptime(time_string, '%H:%M').time()
love = dt.datetime.strptime(time_string, '%H:%M:%S').time()
print(repr(love))
