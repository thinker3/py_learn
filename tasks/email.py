#!/usr/bin/env python
# -*- coding: utf-8 -*-

from invoke import task
from utils.email import send


@task(default=True)
def test(user, password, receiver, host='smtp.qq.com', port=25):
    send(user, password, receiver, host, port)
