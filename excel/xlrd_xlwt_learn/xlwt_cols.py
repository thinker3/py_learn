#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xlwt import Workbook


class Person(object):
    pass


obj = Person()
obj.name = 'chenkun'
obj.age = 27
obj.height = 163
obj.weight = 60

_dict = {'name': 'chenkun', 'age': 27, 'height': 163, 'weight': 61.5}

columns = [
    ['name', '姓名', 8],
    ['age', '年龄', 6],
    ['height', '身高', 6],
    ['weight', '体重', 6],
]

dicts = []
objs = []
for i in range(33):
    objs.append(obj)
    dicts.append(_dict)


def make_xls(sheetname='sheet_1', filename='filename.xls', columns=[], objs=[]):
    book = Workbook()
    sheet = book.add_sheet(sheetname)

    def index_of(key, list_2d):
        for i, one in enumerate(list_2d):
            if key == one[0]:
                return i

    attrs = []
    for inner_list in columns:
        attrs.append(inner_list[0])

    for i in range(len(columns)):
        sheet.write(0, i, columns[i][1])
        sheet.col(i).width = columns[i][2] * 256
    for i, obj in enumerate(objs, start=1):
        for attr in attrs:
            if isinstance(obj, dict):
                sheet.write(i, index_of(attr, columns), obj[attr])
            else:
                sheet.write(i, index_of(attr, columns), getattr(obj, attr))
    book.save(filename)


if __name__ == '__main__':
    make_xls(sheetname='test', filename='abc.xls', columns=columns, objs=objs)
