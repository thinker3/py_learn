from urllib.parse import urlparse
url = 'http://www.163.com'
print(urlparse(url))
url = 'www.163.com'
print(urlparse(url))
print(urlparse(url, 'http'))
url = 'https://www.163.com'
print(urlparse(url, 'http'))
