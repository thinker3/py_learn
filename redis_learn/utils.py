#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
from redis_learn import config


def get_redis(db=1):
    return redis.Redis(host=config.host, port=config.port, db=db)


if __name__ == '__main__':
    db = get_redis()
    __import__('ipdb').set_trace()
