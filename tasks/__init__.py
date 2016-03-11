#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from invoke import Collection
from . import demo
from . import image
from . import email

ns = Collection()  # must be ns?
ns.add_collection(Collection.from_module(demo))
ns.add_collection(Collection.from_module(image))
ns.add_collection(Collection.from_module(email))
