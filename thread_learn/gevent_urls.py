#!/usr/bin/env python
# encoding: utf-8

from gevent import monkey
monkey.patch_all()

import urllib.request, urllib.error, urllib.parse
from gevent.pool import Pool


def download(url):
    return urllib.request.urlopen(url).read()


if __name__ == '__main__':
    urls = ['http://httpbin.org/get'] * 100
    pool = Pool(20)
    r = pool.map(download, urls)
    print(len(r))
    print(r[0])
