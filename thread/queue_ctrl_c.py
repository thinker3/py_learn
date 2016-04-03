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
Queue.running = True
q = Queue.Queue()
for item in tasks:
    q.put(item)


def do_work(item):
    time.sleep(1)
    lock.acquire()
    print(item)
    lock.release()


def worker():
    while Queue.running:
        item = q.get()
        do_work(item)
        if q.empty():
            Queue.running = False

for i in range(worker_number):
     t = threading.Thread(target=worker)
     t.start()

try:
    while Queue.running:
        time.sleep(1)
except KeyboardInterrupt:
    Queue.running = False
