print "3".rjust(2, '0')
print "3".rjust(3, '0')
n = 100
ds = len(str(n))
numbers = map(lambda i: str(i).rjust(ds, '0'), range(1, n))
print ' '.join(numbers)
