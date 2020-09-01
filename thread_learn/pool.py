#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import argparse
import threading
from time import sleep

from utils import redis_utils

redis_conn = redis_utils.get_redis_conn()
queue_name = 'thread_learn.pool'


class Worker(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__isIdle = True
        self.__isDying = False
        self.start()

    @property
    def isIdle(self):
        return self.__isIdle

    def run(self):
        while self.__isDying is False:
            print(f'{self.name} running ...')
            value = redis_utils.get_in_queue(queue_name, timeout=3, redis_conn=redis_conn)
            if value:
                self.__isIdle = False
                self.__handle(value)
        else:
            print(f'{self.name} quitting ...')

    def __handle(self, value):
        #print(f'handling "{value}" ...')
        sleep(random.randint(1, 3))
        #print(f'handling "{value}" done')
        self.__isIdle = True

    def goAway(self):
        self.__isDying = True


class Manager(object):
    sleepInterval = 1

    def __init__(self, minSize=1, maxSize=1):
        assert maxSize >= minSize >= 1
        self.__minSize = minSize
        self.__maxSize = maxSize
        self.__threads = []
        self.__initThreads()

    @property
    def poolSize(self):
        return len(self.__threads)

    @property
    def __idleThreads(self):
        return [one for one in self.__threads if one.isIdle]

    def __initOneThread(self):
        worker = Worker()
        self.__threads.append(worker)

    def __initThreads(self):
        for i in range(self.__minSize):
            self.__initOneThread()

    def __removeOneThread(self, t):
        t.goAway()
        if not t.is_alive():
            self.__threads.remove(t)

    def shutdown(self):
        for t in self.__threads:
            self.__removeOneThread(t)
        print(self.__threads)

    def serve_for_ever(self):
        while True:
            print(f'pool size: {self.poolSize}')
            sleep(self.sleepInterval)
            while len(self.__idleThreads) < 1 and len(self.__threads) < self.__maxSize:
                self.__initOneThread()
                sleep(0.1)
            if len(self.__idleThreads) > 1:
                last = self.__idleThreads[-1]
                if last.isIdle:
                    self.__removeOneThread(last)


def test_server(size):
    manager = Manager(minSize=1, maxSize=size)
    try:
        manager.serve_for_ever()
    except KeyboardInterrupt:
        manager.shutdown()


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
                data = f"{value}-{i + 1}"
                redis_utils.put_in_queue(queue_name, data, redis_conn)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--role', default='server')
    parser.add_argument('-s', '--size', type=int, default=3)
    options = parser.parse_args()
    if options.role == 'server':
        test_server(options.size)
    elif options.role == 'client':
        test_client()
