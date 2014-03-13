l = [1, 5, 3, 2, 7]
print l
print l.sort()
print l

l = [(2, 33.8, 40), (3, 43.15, 10), (4, 37.97, 16), (5, 46.81, 36),
     (6, 48.77, 79), (8, 19.36, 79), (9, 6.76, 64)]
print l
l.sort(key=lambda x: x[1])
print l
l.sort(key=lambda x: x[2])
print l

l = [(2, 33.8, 40), (3, 43.15, 10), (4, 37.97, 16), (5, 46.81, 36),
     (6, 48.77, 79), (8, 19.36, 79), (9, 6.76, 64)]
l.sort(key=lambda x: x[2])
print l
l.sort(key=lambda x: x[1])
print l

l = [(2, 'ab'), (2, 'ac'), (1, 'ad'), (2, 'aa')]
l.sort(key=lambda x: x[0])
print l

import operator
l.sort(key=operator.itemgetter(0, 1))
print l
