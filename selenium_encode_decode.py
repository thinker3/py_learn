from sys import argv
import codecs, time
from selenium.webdriver import Firefox

url = 'http://www.dzsc.com/stock-ic/AD51_025.html'
if len(argv) > 1:
    url = argv[1]
browser = Firefox()
browser.get(url)
time.sleep(0)
html = browser.page_source
print type(html)
try:
    html = codecs.encode(html, 'gbk')
except:
    print 'gbk is not enough'
html = codecs.encode(html, 'gb18030')
print type(html)

f = open('selenium.html', 'w')
f.write(html)
f.close()

browser.close()
