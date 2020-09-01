#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

redis_config = dict(
    host='127.0.0.1',
    port=6380,
    password='root',
)


def get_redis_conn(db=1):
    return redis.Redis(db=db, **redis_config)


def put_in_queue(queue_name, value, redis_conn=None):
    redis_conn = redis_conn or get_redis_conn()
    redis_conn.lpush(queue_name, value)


def get_in_queue(queue_name, block=True, timeout=1, redis_conn=None, **kwargs):
    if kwargs:
        print(kwargs)
    redis_conn = redis_conn or get_redis_conn()
    if block:
        value = redis_conn.brpop(queue_name, timeout=timeout)
    else:
        value = redis_conn.rpop(queue_name)
    return value


if __name__ == '__main__':
    redis_conn = get_redis_conn()
    __import__('ipdb').set_trace()
