#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

host = '127.0.0.1'
port = 6380


def get_redis_conn(db=1):
    return redis.Redis(host=host, port=port, db=db, password='root')


def put_in_queue(queue_name, value, redis_conn=None):
    redis_conn = redis_conn or get_redis_conn()
    redis_conn.lpush(queue_name, value)


def get_in_queue(queue_name, redis_conn=None):
    redis_conn = redis_conn or get_redis_conn()
    value = redis_conn.rpop(queue_name)
    return value


if __name__ == '__main__':
    redis_conn = get_redis_conn()
    __import__('ipdb').set_trace()
