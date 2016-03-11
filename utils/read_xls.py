#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
from utils import get_abs_path


def read_merged_xls(file_contents):
    book = xlrd.open_workbook(file_contents=file_contents)
    data = []
    sheet = book.sheet_by_index(0)
    for rx in range(sheet.nrows):
        line = []
        for ry in range(sheet.ncols):
            cell = sheet.cell_value(rx, ry)
            if not cell:
                cell = data[-1][ry] if data else ''
            line.append(cell)
        data.append(line)
    return data


def read_excel(filepath):
    book = xlrd.open_workbook(filepath)
    sheets = []
    for index in range(book.nsheets):
        sheet = book.sheet_by_index(index)
        data = []
        for rx in range(sheet.nrows):
            line = []
            for ry in range(sheet.ncols):
                cell = sheet.cell_value(rx, ry)
                line.append(cell)
            data.append(line)
        sheets.append(dict(
            name=sheet.name,
            index=index,
            data=data,
        ))
    return sheets


def merged_test():
    file_contents = file('merged.xls').read()
    data = read_merged_xls(file_contents)
    for one in data:
        print one


def sheets_test():
    filepath = get_abs_path(['utils', 'sheets.xlsx'])
    print read_excel(filepath)


if __name__ == '__main__':
    sheets_test()
