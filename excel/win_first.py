#!/usr/bin/env python
# encoding: utf-8

import win32com.client as win32

#excel = win32.gencache.EnsureDispatch('Excel.Application')
#excel = win32.Dispatch('Excel.Application')
excel = win32.DispatchEx('Excel.Application')  # rpac
excel.Visible = 1
#wordBook = excel.Workbooks.open(templatePath)
wordBook = excel.Workbooks.Add()
sheet = wordBook.Sheets(1)
sheet.Cells(1, 1).Value = 'a' * 10
sheet.Cells(1, 2).Value = 'b' * 20
sheet.Cells(2, 2).Value = 'd' * 30

values = sheet.Range(sheet.Cells(1, 1), sheet.Cells(1, 2)).Value
print values
values = sheet.Range(sheet.Cells(1, 1), sheet.Cells(2, 2)).Value
print values

sheet.Range("A5:B5").Value = [['Hello', 'World']]
range = sheet.Range(sheet.Cells(1, 3), sheet.Cells(4, 3))
range.MergeCells = 1
range.Value = 'merged'
cell = sheet.Cells(5, 3)
cell.WrapText = 1
cell.Value = "looooooooooooooooooooooooooooong"

values = sheet.Range(sheet.Cells(1, 1), sheet.Cells(6, 4)).Value
print values

#sheet.Columns("A:A").ColumnWidth = 12
#sheet.Columns("B:B").ColumnWidth = 24
#sheet.Columns("A:B").EntireColumn.AutoFit()
sheet.Columns("A:B").AutoFit()
#wordBook.Close(SaveChanges=0)
#excel.ActiveWorkbook.SaveAs(destinationPath)

"""
excel.Quit()
del excel
"""
