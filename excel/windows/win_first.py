#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import win32com.client as win32

#excel = win32.gencache.EnsureDispatch('Excel.Application')
#excel = win32.Dispatch('Excel.Application')
excel = win32.DispatchEx('Excel.Application')  # rpac
excel.Visible = 0
#workBook = excel.Workbooks.open(templatePath)
workBook = excel.Workbooks.Add()
sheet = workBook.Sheets(1)
sheet.Cells(1, 1).Value = 'a' * 10
sheet.Cells(1, 2).Value = 'b' * 20
sheet.Cells(2, 2).Value = 'd' * 30

values = sheet.Range(sheet.Cells(1, 1), sheet.Cells(1, 2)).Value
print(values)
values = sheet.Range(sheet.Cells(1, 1), sheet.Cells(2, 2)).Value
print(values)

sheet.Range("A5:B5").Value = [['Hello', 'World']]
range = sheet.Range(sheet.Cells(1, 3), sheet.Cells(4, 3))
range.MergeCells = 1
range.Value = 'merged'
cell = sheet.Cells(5, 3)
cell.WrapText = 1
cell.Value = "looooooooooooooooooooooooooooong"

sheet.Range(
        sheet.Cells(1, 4),
        sheet.Cells(5, 4)).Value = "looooooooooooooooooooooooooooong"
#sheet.Columns(4).AutoFit()  # right
sheet.Columns("D").AutoFit()

values = sheet.Range(sheet.Cells(1, 1), sheet.Cells(6, 4)).Value
print(values)

#sheet.Columns("A:A").ColumnWidth = 12
#sheet.Columns("B:B").ColumnWidth = 24
#sheet.Columns("A:B").EntireColumn.AutoFit()
sheet.Columns("A:B").AutoFit()
try:
    #destinationPath = "C:\Users\ken.chen\test.xlsx"  # error
    #destinationPath = r"C:\Users\ken.chen\test.xlsx"
    destinationPath = r"C:\Users\ken.chen\notExists\test.xlsx"
    dirname = os.path.dirname(destinationPath)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    workBook.SaveAs(destinationPath)
    # must close or quit, or the file can not be deleted
    #workBook.Close(SaveChanges=0)
    excel.Quit()

    #destinationPath = "test.xlsx"  # C:\Users\ken.chen\Documents
    #destinationPath = "C:/Users/ken.chen/test.xls"  # error
    #destinationPath = r"C:\Users\ken.chen\test.xls"  # warning
    #destinationPath = r"C:\Users\ken.chen\test.xlsx"
    #workBook.Close(True, destinationPath)
except Exception as e:
    print(e)
    print(e[1])
    print(e[2][2].encode(sys.getfilesystemencoding()))

"""
del excel
"""
