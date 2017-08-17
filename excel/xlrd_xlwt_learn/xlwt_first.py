#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlwt
from xlwt import Workbook

wb = Workbook()
ws = wb.add_sheet('numbers')
for i in xrange(10):
    for j in xrange(10):
        ws.write(i, j, i * j)

ws = wb.add_sheet('letters')
for i in xrange(5):
    for j in xrange(5):
        ws.write(i, j, 'a')

ws = wb.add_sheet('long string')
style = xlwt.XFStyle()
style.alignment.wrap = 1
ws.write(0, 0, 'Hello World Hello World Hello World Hello World Hello World Hello World Hello World', style)
wb.save('First.xls')
