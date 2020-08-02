#!/usr/bin/env python
# encoding: utf-8

import queue
from collections import deque

first_in_first_out = queue.Queue()
first_in_last_out = queue.LifoQueue()
priority_queue = queue.PriorityQueue()

for i in range(5):
    first_in_first_out.put(i)
    first_in_last_out.put(i)

priority_queue.put(5)
priority_queue.put(4)
priority_queue.put(9)
priority_queue.put(2)
priority_queue.put(7)
priority_queue.put(-3)

while not first_in_first_out.empty():
    print(first_in_first_out.get())

print('*' * 30)
while not first_in_last_out.empty():
    print(first_in_last_out.get())

print('*' * 30)
while not priority_queue.empty():
    print(priority_queue.get())


class Person(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __cmp__(self, other):
        return cmp(len(self.name), len(other.name))


priority_queue.put(Person('Jack'))
priority_queue.put(Person('Florance'))
priority_queue.put(Person('Tom'))
priority_queue.put(Person('Susan'))
print('*' * 30)
while not priority_queue.empty():
    print(priority_queue.get())

#Person.__cmp__ = cmp  # not works
#del Person.__cmp__  # strange result
Person.__cmp__ = lambda x, y: cmp(x.name, y.name)
priority_queue.put(Person('Jack'))
priority_queue.put(Person('Florance'))
priority_queue.put(Person('Tom'))
priority_queue.put(Person('Susan'))

print('*' * 30)
while not priority_queue.empty():
    print(priority_queue.get())

print('*' * 30)
queue = queue.Queue()
try:
    queue.get(block=False)
except queue.Empty as e:
    print(('block=False: "%s"' % e))
    print((type(e), repr(e), str(e)))
try:
    queue.get(timeout=1)
except queue.Empty as e:
    print(('timeout=1: "%s"' % e))


def limited_queue_test():
    raw_data = list(range(10))
    dq = deque([], 3)
    for i in raw_data:
        dq.append(i)
    data = []
    while dq:
        data.append(dq.popleft())
    assert data == raw_data[-3:]


limited_queue_test()
