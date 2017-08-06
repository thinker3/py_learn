#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import zipfile

channels = [
    [u'应用宝', 'hzj.qq', u'Hi自驾-让旅游更简单'],
    [u'小米', 'hzj.xiaomi', u'Hi自驾-去旅游吧'],
    [u'百度', 'hzj.baidu', u'Hi自驾-让旅游更简单'],
    [u'360', 'hzj.360', u'Hi自驾-让旅游更简单'],
    [u'魅族', 'hzj.meizu', u'Hi自驾-让旅游更简单'],
    [u'华为', 'hzj.huawei', u'Hi自驾-让旅游更简单'],
    [u'安智', 'hzj.anzhi', u'Hi自驾-让旅游更简单'],
    [u'应用汇', 'hzj.appchina', u'Hi自驾-让旅游更简单'],
    [u'PP助手/阿里/豌豆荚', 'hzj.wandoujia', u'Hi自驾-让旅游更简单'],
    [u'乐商店', 'hzj.lenovo', u'Hi自驾-让旅游更简单'],
    [u'木蚂蚁', 'hzj.mumayi', u'Hi自驾-让旅游更简单'],
    [u'搜狗助手', 'hzj.sogou', u'Hi自驾-让旅游更简单'],
    [u'OPPO', 'hzj.oppo', u'Hi自驾-让旅游更简单'],
    [u'优亿', 'hzj.youyi', u'Hi自驾-让旅游更简单'],
    [u'机锋', 'hzj.jifeng', u'Hi自驾-让旅游更简单'],
    [u'乐视', 'hzj.letv', u'Hi自驾-让旅游更简单'],
    [u'VIVO', 'hzj.vivo', u'Hi自驾-让旅游更简单'],
    [u'三星', 'hzj.sanxing', u'Hi自驾-让旅游更简单'],
    [u'n多市场', 'hzj.nduo', u'Hi自驾-让旅游更简单'],
    [u'爱奇艺', 'hzj.iqiyi', u'Hi自驾-让旅游更简单'],
    [u'金立', 'hzj.jinli', u'Hi自驾-让旅游更简单'],
]
src = 'hzj_release.zip'
if os.path.exists('hzj'):
    shutil.rmtree('hzj')
os.mkdir('hzj')
for one in channels:
    _, url, title = one
    os.makedirs('hzj/%s' % url)
    shutil.copy(src, 'hzj/%s/' % url)
    filename = "META-INF/channel.txt"
    zipped = zipfile.ZipFile('hzj/%s/%s' % (url, src), 'a', zipfile.ZIP_DEFLATED)
    zipped.writestr(filename, url)
    zipped.close()
