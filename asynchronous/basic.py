#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import asyncio


class Record(object):
    def __init__(self, pk, seconds, number):
        self.pk = pk
        self.number = number
        self.seconds = seconds

    def __str__(self):
        return f'<pk: {self.pk}, sleep: {self.seconds}: number: {self.number}>'

    __repr__ = __str__


async def get_int(pk):
    seconds = random.randint(0, 3)
    if seconds == 0:
        raise Exception('0 not allowed')
    await asyncio.sleep(seconds)
    return Record(pk, seconds, random.randint(10, 100))


async def gather():
    tasks = [get_int(i) for i in range(1, 4)]
    res = await asyncio.gather(*tasks, return_exceptions=True)
    print(res)


async def wait():
    tasks = [get_int(i) for i in range(1, 4)]
    done, pending = await asyncio.wait(tasks)
    for one in done:
        try:
            one = one.result()
            print(one)
        except Exception as e:
            print(e)
    print(pending)


def test_gather():
    start = time.perf_counter()
    asyncio.run(gather())
    delta = time.perf_counter() - start
    print(delta)


def test_wait():
    start = time.perf_counter()
    asyncio.run(wait())
    delta = time.perf_counter() - start
    print(delta)


if __name__ == '__main__':
    test_gather()
    test_wait()
