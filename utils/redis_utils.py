#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

host = '127.0.0.1'
port = 6380


def get_redis_conn(db=1):
    return redis.Redis(host=host, port=port, db=db, password='root')


if __name__ == '__main__':
    redis_conn = get_redis_conn()
    __import__('ipdb').set_trace()
