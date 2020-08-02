#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import zipfile

channels = [
    ['应用宝', 'hzj.qq', 'Hi自驾-让旅游更简单'],
    ['小米', 'hzj.xiaomi', 'Hi自驾-去旅游吧'],
    ['百度', 'hzj.baidu', 'Hi自驾-让旅游更简单'],
    ['360', 'hzj.360', 'Hi自驾-让旅游更简单'],
    ['魅族', 'hzj.meizu', 'Hi自驾-让旅游更简单'],
    ['华为', 'hzj.huawei', 'Hi自驾-让旅游更简单'],
    ['安智', 'hzj.anzhi', 'Hi自驾-让旅游更简单'],
    ['应用汇', 'hzj.appchina', 'Hi自驾-让旅游更简单'],
    ['PP助手/阿里/豌豆荚', 'hzj.wandoujia', 'Hi自驾-让旅游更简单'],
    ['乐商店', 'hzj.lenovo', 'Hi自驾-让旅游更简单'],
    ['木蚂蚁', 'hzj.mumayi', 'Hi自驾-让旅游更简单'],
    ['搜狗助手', 'hzj.sogou', 'Hi自驾-让旅游更简单'],
    ['OPPO', 'hzj.oppo', 'Hi自驾-让旅游更简单'],
    ['优亿', 'hzj.youyi', 'Hi自驾-让旅游更简单'],
    ['机锋', 'hzj.jifeng', 'Hi自驾-让旅游更简单'],
    ['乐视', 'hzj.letv', 'Hi自驾-让旅游更简单'],
    ['VIVO', 'hzj.vivo', 'Hi自驾-让旅游更简单'],
    ['三星', 'hzj.sanxing', 'Hi自驾-让旅游更简单'],
    ['n多市场', 'hzj.nduo', 'Hi自驾-让旅游更简单'],
    ['爱奇艺', 'hzj.iqiyi', 'Hi自驾-让旅游更简单'],
    ['金立', 'hzj.jinli', 'Hi自驾-让旅游更简单'],
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
