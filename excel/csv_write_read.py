#!/usr/bin/env python
# encoding: utf-8

# import csv
import codecs
# The csv module doesn’t directly support reading and writing Unicode
import unicodecsv as csv
from utils.csv import UnicodeGBKReader


csv.reader = UnicodeGBKReader


def test():
    with open('test.csv', "wb") as f:
        f.writer(codecs.BOM_UTF8)
        writer = csv.writer(f,
                delimiter='\t', encoding='utf-8',
                quotechar='"', quoting=csv.QUOTE_ALL)
        rows = [
            ['a', 'b', 'c'],
            ['1', '2', '3'],
            ['hello', ',', 'world'],
        ]
        for row in rows:
            # row = ['="%s"' % one for one in row]
            writer.writerow(row)

    with open('test.csv', "rb") as f:
        reader = csv.reader(f,
                delimiter='\t', encoding='utf-8',
                quotechar='"', quoting=csv.QUOTE_ALL)
        for row in reader:
            print(row)


def test_gbk():
    with open('excel/gbk.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in reader:
            print(row)


if __name__ == '__main__':
    test_gbk()
    pass
