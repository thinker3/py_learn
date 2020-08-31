#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading
import requests

tasks = 30
url = 'http://www.baidu.com/'


class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        text = requests.get(url).text
        print((self, len(text)))


class IndependentWorker(Worker):
    pass


class DaemonWorker(Worker):
    def __init__(self):
        super(DaemonWorker, self).__init__()
        self.daemon = True


def main_wait():
    Model = DaemonWorker
    Model = IndependentWorker
    threads = [Model() for i in range(tasks)]
    [t.start() for t in threads]
    [t.join() for t in threads]  # wait until threads done
    print('Over')


def main_no_wait():
    Model = IndependentWorker  # no need to wait IndependentWorker done
    Model = DaemonWorker  # if not wait daemon threads to finish: most likely raised during interpreter shutdown
    [Model().start() for i in range(tasks)]
    time.sleep(1)
    print('Over')


def main_dead_worker_join():
    Model = IndependentWorker
    Model = DaemonWorker
    worker = Model()
    worker.start()
    time.sleep(5)
    print(('worker.is_alive()', worker.is_alive()))
    worker.join()


if __name__ == '__main__':
    # main_wait()
    main_no_wait()
    # main_dead_worker_join()
