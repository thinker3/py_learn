#!/usr/bin/env python
# -*- coding: utf-8 -*-

import happybase

import config

host = config.host
port = 9090  # default
pool = happybase.ConnectionPool(size=3, host=host)

with pool.connection() as connection:
    tables = connection.tables()
    print tables
