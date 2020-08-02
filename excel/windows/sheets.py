#!/usr/bin/env python
# encoding: utf-8

import win32com.client as win32
import pythoncom


def main():
    #pythoncom.CoInitialize()
    excel = win32.DispatchEx('Excel.Application')
    print(excel.Version)
    excel.Visible = 1
    excel.DisplayAlerts = False
    workBook = excel.Workbooks.Add()
    #sheet = workBook.ActiveSheet
    sheet = workBook.Sheets(1)
    sheet.Name = 'a'
    sheet.Cells(1, 1).Value = 'a'
    sheet = workBook.Sheets.Add()
    sheet.Name = 'b'
    sheet.Cells(1, 1).Value = 'b'
    sheet = workBook.Sheets.Add(After=workBook.Sheets(workBook.Sheets.Count))
    sheet.Name = 'c'
    workBook.Sheets(3).Select()


if __name__ == '__main__':
    main()
