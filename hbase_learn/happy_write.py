#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hbase_learn import hbase_utils


def create_table(connection):
    table_name = 'patient'
    if table_name not in connection.tables():
        connection.create_table(
            table_name,
            {
                'profile': dict(),
                'location': dict(),
            },
        )
    table = connection.table(table_name)
    return table


def test_put_one(table):
    info = {
        'profile:name': 'Jack',
        'profile:sex': '1',
        'profile:age': '38',  # can not be number
        # thriftpy.thrift.TDecodeException: Field 'value(3)' of 'Mutation' needs type 'STRING', but the value is `38`
        'location:floor': '8',
        'location:room': 'A012',
        'location:bed': '3',
    }
    row_key = '1'  # can not be number
    table.put(row_key, info)


def test_put_batch(table):
    infos = [
        {
            'profile:name': 'Jim',
            'profile:sex': '1',
            'profile:age': '18',
            'location:floor': '7',
            'location:room': 'B021',
            'location:bed': '2',
        },
        {
            'profile:name': 'Lily',
            'profile:sex': '0',
            'profile:age': '28',
            'location:floor': '6',
            'location:room': 'A011',
            'location:bed': '1',
        },
    ]
    bat = table.batch()
    for i, info in enumerate(infos):
        key = str(i + 2)
        bat.put(key, info)
    bat.send()


def test_delete_row(table):
    row = table.row('3')
    print(row)
    with table.batch() as bat:
        bat.delete('1')
        bat.delete('2')
    rows = list(table.scan())
    print(len(rows))


if __name__ == '__main__':
    connection = hbase_utils.get_connection()
    table = create_table(connection)
    test_put_one(table)
    test_put_batch(table)
    # test_delete_row(table)
    # hbase_utils.delete_table(connection, table.name)
    pass
