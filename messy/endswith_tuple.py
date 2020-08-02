patterns = ['.appspot.com', '.google.com', '.googleusercontent.com', 
            '.googleapis.com', 'googlecode.com', '.gstatic.com', '.google.com.hk']
patterns = tuple(patterns)

host1 = 'code.google.com'
host2 = 'www.baidu.com'

print(host1.endswith(patterns))
print(host2.endswith(patterns))
