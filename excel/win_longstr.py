#!/usr/bin/env python
# encoding: utf-8

import win32com.client as win32

excel = win32.DispatchEx('Excel.Application')
excel.Visible = 0
excel.Visible = 1
wordBook = excel.Workbooks.Add()
sheet = wordBook.Sheets(1)

longstr = (
        """"""
        """WTO members agreed in principle last year to"""
        """ """
        """streamline and standardize global customs rules."""
        """"""
        )
print longstr
sheet.Cells(1, 1).Value = longstr
sheet.Cells(2, 2).Value = longstr
sheet.Cells(3, 3).Value = longstr
sheet.Cells(4, 4).Value = 'short string'
for i in range(1, 5):
    sheet.Columns(i).AutoFit()
print sheet.Columns(1).Width  # 622.5
print sheet.Columns(1).ColumnWidth  # 103.13
for i in range(1, 5):
    sheet.Columns(i).WrapText = 1
    width = sheet.Columns(i).ColumnWidth
    if  width > 24:
        sheet.Columns(i).ColumnWidth = 24
