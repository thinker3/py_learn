#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import asyncio
import argparse

import asyncio_redis

from utils import redis_utils

redis_conn = redis_utils.get_redis_conn(db=0)
channel_name = 'asynchronous.queue'


async def handle(reply):
    await asyncio.sleep(random.randint(1, 3))
    print('Received: ', repr(reply.value), 'on channel', reply.channel)


async def consume():
    connection = await asyncio_redis.Connection.create(**redis_utils.redis_config)
    subscriber = await connection.start_subscribe()
    await subscriber.subscribe([channel_name])
    while True:
        try:
            reply = await subscriber.next_published()
            #task = asyncio.ensure_future(handle(reply))
            task = asyncio.create_task(handle(reply))
            print(task)
        except RuntimeError:
            #connection.close()
            print()
            break


def test_server():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(consume())
    except KeyboardInterrupt:
        loop.close()


def test_client():
    while True:
        text = input('q to quit, e.g.: hello*5 > ')
        if text == 'q':
            break
        else:
            value, times = text.split('*')
            times = int(times)
            assert times >= 1
            for i in range(times):
                message = f"{value}-{i + 1}"
                redis_conn.publish(channel_name, message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--role', default='server')
    options = parser.parse_args()
    if options.role == 'server':
        test_server()
    elif options.role == 'client':
        test_client()
