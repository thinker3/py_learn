import urllib, urllib2, simplejson as json
url = 'https://twitter.com'
proxy = urllib2.ProxyHandler({'https': '127.0.0.1:8088'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
html = urllib2.urlopen(url).read()
f= open('twitter.html', 'w')
f.write(html)
f.close()

