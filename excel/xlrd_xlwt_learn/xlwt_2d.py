#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xlwt import Workbook
from datetime import datetime


class Person(object):
    def __getattr__(self, name):
        return object.__getattribute__(self, name)


obj = Person()
obj.name = 'chenkun'
obj.age = 27
obj.height = 163
obj.weight = 60

_dict = {'name': 'chenkun', 'age': 27, 'height': 163, 'weight': 61.5}

columns = [
    ['name', u'姓名', 8],
    ['age', u'年龄', 6],
    ['height', u'身高', 6],
    ['weight', u'体重', 6],
]

dicts = []
objs = []
for i in xrange(12):
    objs.append(obj)
    dicts.append(_dict)


def get_dotted_attr(obj, dotted_attr):
    attrs = dotted_attr.split('.')
    while attrs:
        attr = attrs.pop(0)
        try:
            obj = getattr(obj, attr)
        except:
            return ''
    return obj


def init_xls(sheetname='1'):
    book = Workbook()
    if sheetname:
        sheet = book.add_sheet(sheetname)
    else:
        sheet = book.add_sheet('1')
    return book, sheet


def save_xls(book, filename='%s.xls' % datetime.now()):
    if filename:
        book.save(filename)
    else:
        filename = '%s.xls' % datetime.now()
        book.save(filename)


def write_xls_1d(sheet, columns=[], objs=[]):
    def index_of(key, list_2d):
        for i, one in enumerate(list_2d):
            if key == one[0]:
                return i

    attrs = []
    for inner_list in columns:
        attrs.append(inner_list[0])

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


col_titles = [
    ['hk', 6],
    ['in', 9],
]
row_titles = ['my', 'his', 'diff']
two_dim_obj = [[100, 200], [10, 250], [90, -50]]


def write_xls_2d(sheet, col_titles=[], row_titles=[], two_dim_obj=[]):
    l = len(sheet.rows)
    for i, one in enumerate(col_titles, start=1):
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


def append(sheet, something, col=0):
    row_num = len(sheet.rows)
    if col:
        sheet.write(row_num, col, something)
    else:
        sheet.write(row_num, 0, something)


def main():
    book, sheet = init_xls(sheetname='1')
    write_xls_1d(sheet, columns, objs)
    write_xls_empty_lines(sheet, num=2)
    write_xls_2d(sheet, col_titles, row_titles, two_dim_obj)
    write_xls_empty_lines(sheet, num=1)
    append(sheet, 'chenkun', len(col_titles))
    save_xls(book, filename='2d.xls')


if __name__ == '__main__':
    main()
