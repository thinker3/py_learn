#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import threading

from utils.log import get_logger
logger = get_logger(__name__)

from utils.redis_utils import get_redis_conn
redis_conn = get_redis_conn()

queue_name = 'redis_list'


class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flag = threading.Event()

    def run(self):
        while not self.flag.is_set():
            value = random.randint(1, 100)
            logger.debug(f'Incoming: {value}')
            redis_conn.lpush(queue_name, value)
            time.sleep(random.randint(3, 5))


class Consumer(threading.Thread):
    def __init__(self, producer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flag = threading.Event()
        self.producer = producer

    def run(self):
        while not self.flag.is_set():
            value = redis_conn.rpop(queue_name)
            logger.debug(f'Outcoming: {value}')
            if value == b'stop':
                self.flag.set()
                self.producer.flag.set()
            else:
                time.sleep(1)


def test_queue():
    producer = Producer()
    consumer = Consumer(producer)

    producer.start()
    consumer.start()

    text = ''
    while text != 'stop':
        text = input("Please input command > ")
        redis_conn.lpush(queue_name, text)
    print('Over')


if __name__ == '__main__':
    test_queue()
