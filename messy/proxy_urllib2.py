import urllib.request, urllib.error, urllib.parse


def main(a, b):
    url = a + '://twitter.com'
    proxy = urllib.request.ProxyHandler({b: '127.0.0.1:8087'})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    html = urllib.request.urlopen(url).read()
    f= open('twitter.html', 'w')
    f.write(html)
    f.close()


# urllib2.URLError: <urlopen error [Errno 10060]
#main('https', 'http')
#main('http', 'https')
#main('http', 'http')

main('https', 'https')  # both should be https
