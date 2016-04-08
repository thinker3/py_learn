#!/usr/bin/env python
# -*- coding: utf-8 -*-

## join and task_done, does not work
## does not need daemon threads

import time
import Queue
import threading

from invoke import task

lock = threading.Lock()
pause = 0.1
worker_number = 10
tasks = range(120)


def do_work(item):
    time.sleep(pause)
    print(item)


def worker(q):
    while Queue.running:
        try:
            item = q.get(timeout=0.1)
            do_work(item)
        except Queue.Empty as e:
            print(type(e), str(e))
        if q.empty():
            Queue.running = False


@task
def main_of_func():
    Queue.running = True
    q = Queue.Queue()
    [q.put(item) for item in tasks]
    [threading.Thread(target=worker, args=(q, )).start() for i in range(worker_number)]
    try:
        while Queue.running:
            time.sleep(1)
    except KeyboardInterrupt:
        Queue.running = False


class Printer(threading.Thread):
    running = True

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        # self.daemon = True

    def run(self):
        while Printer.running:
            if self.queue.empty():
                time.sleep(1)
                Printer.running = False
                break
            try:
                item = self.queue.get(block=False)
                print(item)
            except Queue.Empty as e:
                print(type(e), str(e))


@task
def main_of_class():
    q = Queue.Queue(len(tasks) + 1)
    [q.put(item) for item in tasks]
    [Printer(q).start() for i in range(worker_number)]
    try:
        while Printer.running:
            time.sleep(1)
    except KeyboardInterrupt:
        Printer.running = False


class Useless(threading.Thread):
    running = True

    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data

    def run(self):
        while Useless.running:  # self.running, problematic
            lock.acquire()
            if len(self.data) == 0:
                Useless.running = False  # self.running, problematic
                item = None
            else:
                item = self.data.pop(0)
            lock.release()
            if item is not None:
                time.sleep(pause)
                print(item)


@task
def main_of_useless():
    data = list(tasks)
    [Useless(data).start() for i in range(worker_number)]
    try:
        while Useless.running:
            time.sleep(1)
    except KeyboardInterrupt:
        Useless.running = False

if __name__ == '__main__':
    pass
