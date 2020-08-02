#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gc


def make_cycle():
    d = {}
    d[0] = d
    d = None


def make_container():
    l = []
    l.append(0)
    l.append(2)
    return l


def main():
    print(gc.garbage)
    collected = gc.collect()
    print("Garbage collector: collected %d objects." % (collected))
    make_container()
    print(gc.garbage)
    collected = gc.collect()
    print("Garbage collector: collected %d objects." % (collected))
    print("Creating cycles...")
    for i in range(10):
        make_cycle()
    print(gc.garbage)
    collected = gc.collect()
    print("Garbage collector: collected %d objects." % (collected))
    print(gc.garbage)
    collected = gc.collect()
    print("Garbage collector: collected %d objects." % (collected))


if __name__ == "__main__":
    main()
