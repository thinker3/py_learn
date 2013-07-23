import urllib, urllib2, simplejson as json

def main(a, b):
    url = a + '://twitter.com'
    proxy = urllib2.ProxyHandler({b: '127.0.0.1:8088'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    html = urllib2.urlopen(url).read()
    f= open('twitter.html', 'w')
    f.write(html)
    f.close()

main('https', 'https') # both should be https
