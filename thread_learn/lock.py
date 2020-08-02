#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import threading

from utils.common import get_an_obj

lock = threading.Lock()
obj = get_an_obj()


class MyThread(threading.Thread):
    times = 10

    def run(self):
        if obj.use_lock:
            lock.acquire()
            for i in range(self.times):
                time.sleep(random.random())
                obj.values.append(i)
            lock.release()
        else:
            for i in range(self.times):
                time.sleep(random.random())
                obj.values.append(i)


def test_use_lock_true():
    obj.values = []
    obj.use_lock = True
    threads = [MyThread() for i in range(4)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print(obj.values)


def test_use_lock_false():
    obj.values = []
    obj.use_lock = False
    threads = [MyThread() for i in range(4)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print(obj.values)


if __name__ == '__main__':
    test_use_lock_false()
    test_use_lock_true()
