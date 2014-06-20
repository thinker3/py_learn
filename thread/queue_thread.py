#!/usr/bin/env python
# encoding: utf-8

import threading
import Queue
import time, random

WORKERS = 5
lock = threading.Lock()


class Worker(threading.Thread):
    def __init__(self, queue):
        self.__queue = queue
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            item = self.__queue.get()
            if item is None:
                lock.acquire()
                print self.name, 'quits'
                lock.release()
                break
            time.sleep(random.randint(10, 100) / 1000.0)  # integers in [10, 100]
            lock.acquire()
            print self.name, "task", item, "finished"
            lock.release()

# class Queue.Queue(maxsize=0)
# maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue.
# Insertion will block once this size has been reached, until queue items are consumed.
# If maxsize is less than or equal to zero, the queue size is infinite.
queue = Queue.Queue()
for i in range(WORKERS):
    Worker(queue).start()

for i in range(50):
    queue.put(i)

for i in range(WORKERS):
    queue.put(None)
