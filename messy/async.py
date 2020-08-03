#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import asyncio


async def get_int(seconds=0):
    if seconds == 0:
        raise Exception('0 not allowed')
    await asyncio.sleep(seconds)
    return random.randint(10, 100)


async def main():
    res = await asyncio.gather(get_int(), get_int(3), get_int(5))
    print(res)


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    delta = time.perf_counter() - start
    print(delta)
