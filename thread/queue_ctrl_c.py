#!/usr/bin/env python
# -*- coding: utf-8 -*-

## join and task_done, does not work
## does not need daemon threads

import time
import Queue
import threading

lock = threading.Lock()
worker_number = 3
tasks = range(12)


def do_work(item):
    time.sleep(1)
    lock.acquire()
    print(item)
    lock.release()


def worker(q):
    while Queue.running:
        item = q.get()
        do_work(item)
        if q.empty():
            Queue.running = False


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

    def run(self):
        while self.running:
            if self.queue.empty():
                self.running = False
            task = self.queue.get()
            lock.acquire()
            time.sleep(1)
            print(task)
            lock.release()


def main_of_class():
    q = Queue.Queue()
    [q.put(item) for item in tasks]
    [Printer(q).start() for i in range(worker_number)]
    try:
        while Printer.running:
            time.sleep(1)
    except KeyboardInterrupt:
        Printer.running = False

# main_of_func()
main_of_class()
