#!/usr/bin/env python
# -*- coding: utf-8 -*-

import peewee
from . import config
from playhouse.pool import PooledMySQLDatabase

mysqldb = PooledMySQLDatabase(
    'test',
    user=config.user,
    passwd=config.passwd,
    max_connections=90,
    stale_timeout=300,
)


class Bar(peewee.Model):
    length = peewee.IntegerField(null=True)

    class Meta:
        database = mysqldb


def init_models():
    for cls in list(globals().values()):
        if type(cls) == peewee.BaseModel:
            try:
                if hasattr(cls, 'create_table'):
                    cls.create_table()
            except peewee.OperationalError as e:
                print(e)

if __name__ == '__main__':
    init_models()
