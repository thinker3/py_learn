#!/usr/bin/env python
# encoding: utf-8

import csv


ofile  = open('test.csv', "wb")
writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
rows = [
        ['a', 'b', 'c'],
        ['1', '2', '3'],
        ['hello', ',', 'world'],
        ]
for row in rows:
    writer.writerow(row)
ofile.close()


ifile = open('test.csv', "rb")
reader = csv.reader(ifile, delimiter='\t', quoting=csv.QUOTE_ALL)
for row in reader:
    print row
ifile.close()
