#!/usr/bin/env python
# -*- coding: utf-8 -*-

import happybase

from . import config

host = config.host
port = 9090  # default


def get_connection():
    connection = happybase.Connection(host=host)
    return connection


def get_table(connection, table_name):
    table = connection.table(table_name)
    return table


def delete_table(connection, table_name):
    return connection.delete_table(table_name, disable=True)


def get_count(table):
    rows = list(table.scan())
    count = len(rows)
    return count


def row_to_dicts(row):
    dicts = {}
    for k, v in row.items():
        k1, k2 = k.split(':')
        dicts.setdefault(k1, {}).update({k2: v})
    return dicts


if __name__ == '__main__':
    pass
