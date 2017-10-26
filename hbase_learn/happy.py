#!/usr/bin/env python
# -*- coding: utf-8 -*-

import happybase

host = '172.18.0.5'
port = 9090  # default
connection = happybase.Connection(host=host)
tables = connection.tables()
table_name = 'patient'
if table_name not in tables:
    connection.create_table(
        table_name,
        {
            'info': dict(),
        },
    )
table = connection.table(table_name)
info = {
    'info:name': 'Jack',
    'info:sex': '1',
    'info:age': '38',
}
row_key = '1'  # can not be int
table.put(row_key, info)
row = table.row(row_key)
print row

infos = [
    {
        'info:name': 'Jim',
        'info:sex': '1',
        'info:age': '18',
    },
    {
        'info:name': 'Lily',
        'info:sex': '0',
        'info:age': '28',
    },
]
bat = table.batch()
for i, info in enumerate(infos):
    key = str(i + 2)
    bat.put(key, info)
bat.send()
row = table.row('3')
print row
with table.batch() as bat:
    bat.delete('1')
    bat.delete('2')
rows = list(table.scan())
print len(rows)
