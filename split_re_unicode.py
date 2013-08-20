#coding=utf8
import re
s_list = [
    'abc,edf',
    'abc, edf',
    'abc ,edf',
    'abc , edf',
    'abc  , edf',
    'abc ,  edf',
    'abc :  edf',
    u'abc，edf', # a leading 'u' is needed
    ]
p = re.compile(ur'\s*[,:，]\s*')
for one in s_list:
    r = p.split(one)
    print r
