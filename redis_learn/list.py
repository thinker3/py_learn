#!/usr/bin/env python
# -*- coding: utf-8 -*-

from redis_learn import utils


def fix_length_list():
    db = utils.get_redis()
    db.delete('li')
    db.lpush('li', 6, 5, 4)
    db.ltrim('li', 0, 4)
    li = db.lrange('li', 0, -1)
    print li
    db.lpush('li', 3, 2, 1)
    db.ltrim('li', 0, 4)
    li = db.lrange('li', 0, -1)
    print li


fix_length_list()
