#!/usr/bin/env python
# encoding: utf-8


from gevent import monkey
import socket
print socket.socket
monkey.patch_socket()
print socket.socket

import select
print select.select
monkey.patch_select()
print select.select

import urllib2
import gevent
import simplejson as json


def fetch(pid):
    protocol = 'http'
    proxy = urllib2.ProxyHandler({protocol: '127.0.0.1:8087'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    url = '%s://date.jsontest.com' % protocol
    response = urllib2.urlopen(url)
    result = response.read()
    json_result = json.loads(result)
    time = json_result['time']

    print('Process %s: %s' % (pid, time))
    return json_result['time']


def synchronous():
    for i in range(1,10):
        fetch(i)


def asynchronous():
    threads = []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
