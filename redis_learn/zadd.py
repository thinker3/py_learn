#!/usr/bin/env python
# -*- coding: utf-8 -*-

from redis_learn import utils


def test_zadd():
    db = utils.get_redis()
    db.zadd('location', 'a', 1)
    db.zadd('location', 'b', 5)
    db.zadd('location', 'c', 3)
    db.zadd('location', 'd', 4)
    print db.zrangebyscore('location', '0', '5')
    print db.zrangebyscore('location', 1, 4)


if __name__ == '__main__':
    test_zadd()
    pass
