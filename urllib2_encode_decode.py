import urllib2
from sys import argv

url = 'http://www.dzsc.com/stock-ic/AD51_025.html'
if len(argv) > 1:
    url = argv[1]
html = urllib2.urlopen(url, timeout=5).read()
print type(html)
html = html.decode('gbk')
print type(html)
html = html.encode('gbk')
print type(html)

f = open('urllib2.html', 'w')
f.write(html)
f.close()
