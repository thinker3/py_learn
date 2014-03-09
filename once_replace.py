from sys import argv


def get_replaced(s, t):
    for i in xrange(1, len(t), 2):
        s = s.replace(t[i - 1], '(%d)' % (i + 1))
    for i in xrange(2, len(t) + 1, 2):
        s = s.replace('(%d)' % i, t[i - 1])
    return s

f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        s, t = one.split(';')
        t = t.split(',')
        print get_replaced(s, t)
f.close()
