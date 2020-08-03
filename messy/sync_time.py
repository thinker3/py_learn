#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from datetime import (
    datetime,
    timedelta,
)

import requests


def get_webservertime(host):
    response = requests.head(host)
    dts = response.headers['Date'][5:-4]
    server_dt = datetime.strptime(dts, "%d %b %Y %H:%M:%S") + timedelta(hours=8)
    local_dt = datetime.now()
    if (server_dt > local_dt):
        diff = server_dt - local_dt
    else:
        diff = local_dt - server_dt
    print(diff.seconds)
    if (diff.seconds > 30):
        os.system('sudo ntpdate -u time.apple.com')

get_webservertime('http://www.baid.com')
