from sys import argv
import itertools

def remove_non_relevant(a, b):
    a = a.strip()
    set_a = set(a)
    set_b = set(b)
    for i in set_a - set_b:
        a = a.replace(i, '')
    for i in set_b - set_a:
        b = b.replace(i, '')
    return a, b

def order_by_len(a, b):
    if len(a) <= len(b):
        return a, b
    else:
        return b, a

def is_subsequence(less, more):
    last = -1
    for i in less:
        try:
            j = more.index(i, last+1)
            last = j
        except:
            return False
    return True

def get_max_subsequence(a, b):
    a, b = order_by_len(*remove_non_relevant(a, b))
    if not a:
        return 0
    for i in xrange(len(a), 0, -1):
        for one in itertools.combinations(a, i):
            if one[-1] == ' ':
                continue
            if is_subsequence(one, b):
                return ''.join(one)

f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        s1, s2 = one.split(';')
        print get_max_subsequence(s1, s2)
f.close()
