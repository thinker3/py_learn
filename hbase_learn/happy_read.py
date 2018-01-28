#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils


def seperate(n=120):
    print '*' * n


def test_row(table, row_key):
    row = table.row(row_key)
    assert isinstance(row, dict)
    for k, v in row.iteritems():
        print k, v
    row = utils.row_to_dicts(row)
    for k, v in row.iteritems():
        print k, v
    seperate(80)


def test_scan(table):
    rows = table.scan()
    for row_key, row in rows:
        print row_key, row


def test_counter(table, row_key):
    print table.counter_get('1', 'profile:counter')
    print table.row(row_key)
    print table.counter_inc('1', 'profile:counter', 2)
    print table.row(row_key)


if __name__ == '__main__':
    connection = utils.get_connection()
    tables = connection.tables()
    assert isinstance(tables, list)
    print tables
    table_name = 'patient'
    table = utils.get_table(connection, table_name)
    assert table.name == table_name
    # print table.regions()  # TTransportException: TTransportException(message='TSocket read 0 bytes', type=4)
    families = table.families()
    keys = families.keys()
    print keys
    # table.count()  # no count available
    seperate()
    test_scan(table)
    seperate()
    test_row(table, '1')
    test_row(table, '2')
    test_row(table, '3')
    pass
