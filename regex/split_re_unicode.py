# coding=utf8
import re
s_list = [
    'abc,edf',
    'abc, edf',
    'abc ,edf',
    'abc , edf',
    'abc  , edf',
    'abc ,  edf',
    'abc :  edf',
    'abc，edf',  # a leading 'u' is needed
]
p = re.compile(r'\s*[,:，]\s*')
for one in s_list:
    r = p.split(one)
    print(r)

s = 'a;b;c;d'
print(s.split(';', 1))  # ['a', 'b;c;d']
print(s.split(';', 2))  # ['a', 'b', 'c;d']

s = 'a__b__c__d'
print(s.split('__'))
