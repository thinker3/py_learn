#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyaxmlparser import APK

info = APK('./driver-envrelease-release-1.3.0.apk')
print((info.version_name))
print((info.version_code))
