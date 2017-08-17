#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import (
    datetime,
)
import xlrd
from xlwt import Workbook
import urllib
from utils import get_abs_path
try:
    from django.http import HttpResponse
except:
    HttpResponse = None


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


def get_attrs(columns):
    attrs = []
    for inner_list in columns:
        attrs.append(inner_list[0])
    return attrs


def get_dotted_attr(obj, dotted_attr):
    attrs = dotted_attr.split('.')
    while attrs:
        attr = attrs.pop(0)
        try:
            obj = getattr(obj, attr)
        except:
            return ''
    return obj


def index_of(key, list_2d):
    for i, one in enumerate(list_2d):
        if key == one[0]:
            return i


def write_xls_one_line(sheet, columns):
    l = len(sheet.rows)
    for i in xrange(len(columns)):
        sheet.write(l, i, columns[i])


def write_xls_lines(sheet, data_of_columns):
    l = len(sheet.rows)
    for columns in data_of_columns:
        for i in xrange(len(columns)):
            sheet.write(l, i, columns[i])
        l += 1


def write_xls_1d(sheet, columns=[], objs=[]):
    attrs = get_attrs(columns)
    l = len(sheet.rows)
    for i in xrange(len(columns)):
        sheet.write(l, i, columns[i][1])
        sheet.col(i).width = columns[i][2] * 256
    for i, obj in enumerate(objs, start=l + 1):
        for attr in attrs:
            if isinstance(obj, dict):
                sheet.write(i, index_of(attr, columns), obj[attr])
            else:
                sheet.write(i, index_of(attr, columns), get_dotted_attr(obj, attr))


def write_xls_2d(sheet, col_titles=[], row_titles=[], two_dim_obj=[]):
    l = len(sheet.rows)
    for i, one in enumerate(col_titles, start=0):
        sheet.write(l, i, one[0])
        sheet.col(i).width = one[1] * 256
    for i, one in enumerate(row_titles, start=l + 1):
        sheet.write(i, 0, one)
    for i, r in enumerate(two_dim_obj, start=l + 1):
        for j, c in enumerate(r, start=1):
            sheet.write(i, j, c)


def write_xls_empty_lines(sheet, num=0):
    l = len(sheet.rows)
    if num <= 0:
        return
    else:
        for i in range(l, num + l):
            sheet.write(i, 0, '')


def append_xls_with(sheet, something, col=0):
    row_num = len(sheet.rows)
    if col:
        sheet.write(row_num, col, something)
    else:
        sheet.write(row_num, 0, something)


def make_workbook_with_one_sheet(sheetname, filename, columns, objs):
    book = Workbook()
    sheet = book.add_sheet(sheetname)
    attrs = get_attrs(columns)
    for i in xrange(len(columns)):
        sheet.write(0, i, columns[i][1])
        sheet.col(i).width = columns[i][2] * 256
    for i, obj in enumerate(objs, start=1):
        for attr in attrs:
            if isinstance(obj, dict):
                sheet.write(i, index_of(attr, columns), obj[attr])
            else:
                sheet.write(i, index_of(attr, columns), get_dotted_attr(obj, attr))
    if not filename:
        filename = '%s.xls' % datetime.now()
    return book, filename


def make_workbook(filename=None):
    book = Workbook()
    if not filename:
        filename = '%s.xls' % datetime.now()
    return book, filename


def make_sheet(book, columns, objs, sheetname='1'):
    sheet = book.add_sheet(sheetname)
    write_xls_1d(sheet, columns, objs)


def make_xls_file(sheetname='1', filename=None, columns=[], objs=[]):
    book, filename = make_workbook_with_one_sheet(sheetname, filename, columns, objs)
    book.save(filename)


def make_xls_response(sheetname='1', filename=None, columns=[], objs=[]):
    book, filename = make_workbook_with_one_sheet(sheetname, filename, columns, objs)
    response = HttpResponse(mimetype='application/vnd.ms-excel')
    # "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    response = HttpResponse(content_type='application/vnd.ms-excel')
    filename = urllib.quote(unicode(filename).encode('utf8'))
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    book.save(response)
    return response


def init_xls(sheetname='1'):
    book = Workbook()
    if sheetname:
        sheet = book.add_sheet(sheetname)
    else:
        sheet = book.add_sheet('1')
    return book, sheet


def save_xls(book, filename=None):
    if filename:
        book.save(filename)
    else:
        filename = '%s.xls' % datetime.now()
        book.save(filename)


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
