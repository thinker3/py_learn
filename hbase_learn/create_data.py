#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from utils import common
from hbase_learn import hbase_utils


def create_table(connection):
    table_name = 'for_phoenix'
    if table_name not in connection.tables():
        connection.create_table(
            table_name,
            {
                'A': dict(),
            },
        )
    table = connection.table(table_name)
    return table


def create_one():
    key = common.get_uuid()
    create_time = common.get_now_str()
    return dict(
        create_time=create_time,
        key=key,
        name=key,
        age=random.randint(1, 65),
        sex=random.choice(['male', 'female']),
        deleted=random.choice([True, False]),
    )


def create_many(table, count=10000):
    for i in xrange(count):
        print i
        data = create_one()
        row_key = '{key}__{create_time}'.format(**data)
        temp = {}
        for k, v in data.iteritems():
            temp['A:%s' % k] = common.convert_to_string(v)
        print temp
        table.put(row_key, temp)


if __name__ == '__main__':
    connection = hbase_utils.get_connection()
    table = create_table(connection)
    create_many(table)
