#!/usr/bin/env python
# encoding: utf-8

import psutil

keys = [
    'pid',
    'username',
    'name',
    'exe',
    'cmdline',
]

for proc in psutil.process_iter():
    d = proc.as_dict()
    for key in keys:
        print('%s: %s' % (key, d[key]))
    print()

'''
pid: 895
username: root
name: getty
exe: /sbin/getty
cmdline: ['/sbin/getty', '-8', '38400', 'tty6']

pid: 1574
username: phy
name: python
exe: /usr/bin/python2.7
cmdline: ['python', '/home/phy/nuts/git/goagent/local/proxy.py']
'''

'''
pid: 3008
username: YOS-01411032321\Administrator
name: NutstoreWatchDog.exe
exe: C:\Program Files\nuts\bin-3.2.1\NutstoreWatchDog.exe
cmdline: []

pid: 3668
username: YOS-01411032321\Administrator
name: python.exe
exe: C:\Python27\python.exe
cmdline: ['python', 'C:\\Users\\Administrator\\nuts\\git\\youdao\\my_youdao.py']

pid: 3924
username: YOS-01411032321\Administrator
name: gvim.exe
exe: C:\Program Files (x86)\Vim\vim74\gvim.exe
cmdline: ['C:\\Program Files (x86)\\Vim\\vim74\\gvim.exe', '-p', 'psutil_learn.py']

pid: 4296
username: YOS-01411032321\Administrator
name: python.exe
exe: C:\Python27\python.exe
cmdline: ['python', 'psutil_learn.py']
'''
