#!/usr/bin/env python
# -*- coding: utf-8 -*-

from invoke import task


@task(default=True)
def test(under_score='1'):
    # invoke demo --under-score=0
    print('test under_score', under_score)


@task
def pysocks(host='www.twitter.com', port=443):
    import socks
    s = socks.socksocket()
    s.set_proxy(socks.SOCKS5, "127.0.0.1")  # SOCKS4 and SOCKS5 use port 1080 by default
    s.connect((host, port))
    s.sendall("GET / HTTP/1.1 \r\n\r\n")
    print s.recv(4096)
