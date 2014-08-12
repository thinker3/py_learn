import urllib2


def main(a, b):
    url = a + '://twitter.com'
    proxy = urllib2.ProxyHandler({b: '127.0.0.1:8087'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    html = urllib2.urlopen(url).read()
    f= open('twitter.html', 'w')
    f.write(html)
    f.close()


# urllib2.URLError: <urlopen error [Errno 10060]
#main('https', 'http')
#main('http', 'https')
#main('http', 'http')

main('https', 'https')  # both should be https
