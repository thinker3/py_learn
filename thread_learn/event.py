#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import threading


class Worker(threading.Thread):
    def run(self):
        for i in range(10):
            print(self, i)
            time.sleep(random.random())


class EventWorker(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flag = threading.Event()

    def run(self):
        while not self.flag.is_set():
            print('beating...')
            time.sleep(1)


def test_event():
    worker_one = Worker()
    worker_two = Worker()
    event = EventWorker()

    event.start()
    worker_one.start()
    worker_two.start()
    worker_one.join()
    worker_two.join()
    event.flag.set()
    event.join()  # here it is not needed?
    print('Over')


if __name__ == '__main__':
    test_event()
