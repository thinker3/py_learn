#!/usr/bin/env python
# -*- coding: utf-8 -*-

import axmlparserpy.apk as apk

info = apk.APK('./driver-envrelease-release-1.3.0.apk')

print info.get_package()
print info.get_androidversion_name()
print info.get_androidversion_code()

print info.androidversion
print info.androidversion_name
print info.androidversion_code
