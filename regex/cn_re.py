#coding=utf8
import re
a=u'不要家私的勿扰'
aa=u'不需要家私的勿扰'
aaa=u'不要家私者勿扰'
aaaa=u'不需要家私者勿扰'
p=ur'不需?要家私[的者]勿扰'
b=re.search(p, a, re.I).group()
c=re.search(p, aa, re.I).group()
d=re.search(p, aaa, re.I).group()
e=re.search(p, aaaa, re.I).group()
print b, c, d, e
