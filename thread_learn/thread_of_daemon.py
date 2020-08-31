#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import queue
import argparse
import threading

cache = queue.Queue()


class Fetcher(threading.Thread):
    def __init__(self, word, daemon, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.word = word
        self.daemon = daemon

    def run(self):
        while True:
            print(f"fetching {self.word} ...")
            time.sleep(1)


class Manager(threading.Thread):
    def __init__(self, subdaemon, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.daemon = True
        self.subdaemon = subdaemon

    def run(self):
        while True:
            word = cache.get()
            Fetcher(word, self.subdaemon).start()


def test(subdaemon):
    Manager(subdaemon).start()
    for word in ['hello', 'world']:
        cache.put(word)
    time.sleep(1000)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--daemon', action='store_true')
    options = parser.parse_args()
    try:
        test(options.daemon)
    except KeyboardInterrupt:
        print()
