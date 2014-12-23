#!/usr/bin/env python
# encoding: utf-8

import win32com.client as win32

excel = win32.DispatchEx('Excel.Application')
excel.Visible = 1
workBook = excel.Workbooks.Add()
sheet = workBook.Sheets(1)

start_row = 2
row = 5

sheet.Cells(1, 1).Value = 'Number'
for i in range(start_row, start_row+row):
    sheet.Cells(i, 1).Value = i - 1

summed = sheet.Range(
        sheet.Cells(start_row, 1),
        sheet.Cells(start_row + row - 1, 1)
    )
# color
#summed.Interior.ColorIndex = 6  # yellow
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

delta = 2
start_column = used.Column + used.Columns.Count
sheet.Range(sheet.Columns(start_column), sheet.Columns(start_column + delta)).ColumnWidth = 2
start_row = used.Row + used.Rows.Count
sheet.Range(sheet.Rows(start_row), sheet.Rows(start_row + delta)).RowHeight = 50


def get_column_number(letter):
    # get column number by column letter
    col = sheet.Columns(letter).Column
    print col

letter = 'c'
get_column_number(letter)
letter = 'ab'
get_column_number(letter)


def dollar():
    # number or text(string)
    #cell.NumberFormatLocal = "@"
    cell = sheet.Cells(1, 1)
    cell.Value = '8'
    cell.NumberFormat = "@"
    cell = sheet.Cells(1, 2)
    cell.Value = 8
    cell.NumberFormat = "@"
    cell = sheet.Cells(1, 3)
    # even if the value is of format text(string)
    cell.Value = 'abc'
    cell.NumberFormat = "@"

    cell = sheet.Cells(1, 4)
    cell.Value = '8'
    cell = sheet.Cells(1, 5)
    cell.Value = 8

dollar()


def delete_row(row_number):
    sheet.Rows(row_number).EntireRow.Delete()

#delete_row(10)
