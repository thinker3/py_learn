#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import win32com.client as win32

excel = win32.DispatchEx('Excel.Application')
excel.Visible = 0
home = os.path.expanduser('~')


def copy_save_xls(data):
    workBook = excel.Workbooks.Add()
    sheet = workBook.Sheets(1)
    rows = len(data)
    cols = len(data[0])
    sheet.Range(sheet.Cells(1, 1), sheet.Cells(rows, cols)).Value = data
    try:
        sheet.Cells(1, 1).Value = 'test'
        destinationPath = os.path.join(home, 'copy.xls')
        workBook.SaveAs(destinationPath)
        workBook.Close(SaveChanges=0)
    except Exception as e:
        print(e)


def save_xls():
    xls = os.path.abspath('excel_2003.xls')
    workBook = excel.Workbooks.Open(xls)
    sheet = workBook.ActiveSheet
    data = sheet.UsedRange.Rows.Value
    copy_save_xls(data)
    try:
        sheet.Cells(1, 1).Value = 'test'
        destinationPath = os.path.join(home, 'excel_2003.xls')
        workBook.SaveAs(destinationPath, FileFormat=56)  # 2003
        workBook.Close(SaveChanges=0)
    except Exception as e:
        print(e)

save_xls()
