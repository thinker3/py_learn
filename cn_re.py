#coding=utf8
import re
x=u'需'
print x.encode('utf8').__repr__()
a=u'不要家私的勿扰'.encode('utf8')
aa=u'不需要家私的勿扰'.encode('utf8')
p=u'不需?要'.encode('utf8')
print p.__repr__()
b=re.findall(p, a, re.I)
for one in b:
    print one
