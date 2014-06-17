#!/usr/bin/env python
# encoding: utf-8

import win32com.client as win32

excel = win32.DispatchEx('Excel.Application')
excel.Visible = 1
wordBook = excel.Workbooks.Add()
sheet = wordBook.Sheets(1)

start_row = 2
row = 5

sheet.Cells(1, 1).Value = 'Number'
for i in range(start_row, start_row+row):
    sheet.Cells(i, 1).Value = i - 1

summed = sheet.Range(
        sheet.Cells(start_row, 1),
        sheet.Cells(start_row + row - 1, 1)
    )
#summed.Interior.ColorIndex = 6
summed.Interior.Color = 65535

# where 7 through 13 correspond to borders for (xlEdgeTop, xlEdgeBottom, xlEdgeRight, xlEdgeLeft, xlInsideHorizontal, xlInsideVertical)
# LineStyle of 1 = xlContinous
# Weight of 2 = xlThin

for border_id in range(7, 13):
    summed.Borders(border_id).LineStyle=1
    summed.Borders(border_id).Weight=2

points = {
    'first': start_row, 
    'second': 1, 
    'third':start_row + row - 1, 
    'fourth': 1, 
}
formula = "=sum(r%(first)sc%(second)s:r%(third)sc%(fourth)s)" % points
print formula  # =sum(r2c1:r6c1)
sheet.Cells(start_row + row, 1).FormulaR1C1 = formula

sheet.Cells(2, 4).Value = '2.4'

used = sheet.UsedRange
#print used
print used.Row, used.Column
print used.Rows.Count, used.Columns.Count 

# insert empty row, column
sheet.Columns(1).EntireColumn.Insert()
print used.Row, used.Column
print used.Rows.Count, used.Columns.Count 

sheet.Rows(1).EntireRow.Insert()
print used.Row, used.Column
print used.Rows.Count, used.Columns.Count 
