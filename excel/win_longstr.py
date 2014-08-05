#!/usr/bin/env python
# encoding: utf-8

import os
import win32com.client as win32
from win32com.client import constants
from win32com.client import makepy


def get_constants_using_EnsureModule():
    makepy_path = os.path.abspath(makepy.__file__)
    cmd = '''python %s''' % makepy_path
    print cmd
    from win32com.client import gencache
    gencache.EnsureModule('{00020813-0000-0000-C000-000000000046}', 0, 1, 6)
    excel = win32.DispatchEx('Excel.Application')
    return excel


def get_constants_using_makepy():
    makepy_path = os.path.abspath(makepy.__file__)
    lib = "Microsoft Excel 12.0 Object Library"
    cmd = '''python %s "%s"''' % (makepy_path, lib)
    print cmd
    os.popen(cmd)
    """
    If Excel is already open, using dispatch will create a new tab in the Excel instance.
    Using dispatchEx will open a new instance of Excel.
    Use DispatchEx instead of Dispatch for dynamic languages.
    """
    excel = win32.DispatchEx('Excel.Application')
    return excel


def get_constants_using_EnsureDispatch():
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    return excel


def main(excel):
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
    print sheet.Columns(1).Width  # 622.5
    print sheet.Columns(1).ColumnWidth  # 103.13
    # AttributeError: Property '<unknown>.Width' can not be set.
    #sheet.Columns(1).Width = 100
    sheet.Cells(5, 5).Value = 'centered'
    sheet.Columns(5).ColumnWidth = 24
    sheet.Rows(5).RowHeight = 30 
    sheet.Columns(5).HorizontalAlignment = constants.xlCenter
    #sheet.Columns(5).VerticalAlignment = constants.xlBottom
    sheet.Columns(1).Font.Color = 24832
    sheet.Cells(2, 2).Interior.Color = 13561798
    sheet.Columns(3).Font.Bold = True


if __name__ == '__main__':
    #excel = get_constants_using_EnsureModule()
    #excel = get_constants_using_makepy()
    excel = get_constants_using_EnsureDispatch()
    main(excel)
