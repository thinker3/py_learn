import urllib2
from sys import argv
import codecs


html = urllib2.urlopen(argv[1], timeout=5).read()

f = open('1.html', 'w')
f.write(html)
f.close()

print codecs.decode(html, 'gbk')

f = codecs.open('1.html', 'r', 'gbk')
html = f.read()
f.close()
#print html

