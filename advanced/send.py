#!/usr/bin/env python
# encoding: utf-8


def countdown(n):
    print("Counting down from", n)
    while n >= 0:
        new_value = (yield n)
        # If a new value got sent in, reset n with it
        if new_value is not None:
            n = new_value
        else:
            n -= 1

c = countdown(5)
for m in c:
    print(m)
    if m == 5:
        m = c.send(3)
        print(m)


def countdown(n):
    print("Counting down from", n)
    while n >= 0:
        yield n
        n -= 1

c = countdown(5)
for m in c:
    print(m)
    if m == 5:
        m = c.send(3)
        print(m)
