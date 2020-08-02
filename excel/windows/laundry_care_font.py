#!/usr/bin/env python
# encoding: utf-8

import win32com.client as win32


def main():
    excel = win32.DispatchEx('Excel.Application')
    excel.Visible = 0
    excel.Visible = 1
    workBook = excel.Workbooks.Add()
    sheet = workBook.Sheets(1)

    gFont = "GLOBAL Care Icon"
    jFont = "JapaneseNext"

    #sheet.Cells(1, 1).Value = 'ź'
    sheet.Cells(1, 1).Value = 'ź'
    sheet.Cells(1, 1).Font.Name = gFont

    sheet.Cells(2, 2).Value = 'A'
    sheet.Cells(2, 2).Font.Name = gFont

    sheet.Cells(3, 3).Value = 'E'
    sheet.Cells(3, 3).Font.Name = jFont
    for i in range(1, 4):
        sheet.Columns(i).Font.Size = 30


if __name__ == '__main__':
    main()
