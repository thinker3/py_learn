#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import threading


class Worker(threading.Thread):
    def run(self):
        for i in range(20):
            print(self, i)
            time.sleep(random.random())


class DaemonWorker(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.daemon = True

    def run(self):
        while True:
            print('beating...')
            time.sleep(1)


def test_daemon():
    worker_one = Worker()
    worker_two = Worker()
    daemon = DaemonWorker()

    daemon.start()
    worker_one.start()
    worker_two.start()
    # daemon.join()  # don't do this, always beating
    worker_one.join()  # main thread wait until worker_one done
    worker_two.join()  # main thread wait until worker_two done
    print('Over')


if __name__ == '__main__':
    test_daemon()
