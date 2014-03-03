import itertools
from sys import argv

def get_overlap_number_sub(a, b):
    len_a, len_b = map(len, (a, b))
    b0 = b[0]
    try:
        j = a.index(b0)
        le_a = len_a-j
        if le_a == 1:
            return 1
        for i in xrange(1, min(le_a, len_b)):
            if a[i+j] != b[i]:
                return get_overlap_number_sub(a[j+1:], b)
        else:
            return i + 1
    except:
        return 0


def get_overlap_number(a, b):
    m = max(get_overlap_number_sub(a, b), get_overlap_number_sub(b, a))
    return m

def merge(a, b):
    i = get_overlap_number_sub(a, b)
    j = get_overlap_number_sub(b, a)
    if i>j:
        return a + b[i:]
    else:
        return b + a[j:]

def concat(one):
    fragments = one.split(';')
    while len(fragments) > 1:
        n = len(fragments)
        the_max = 0
        index = None
        for i, j in itertools.combinations(range(n), 2):
            m = get_overlap_number(fragments[i], fragments[j])
            if m > the_max:
                the_max = m
                index = i, j
        if index:
            i, j = index
            merged = merge(fragments[i], fragments[j])
            fragments.pop(j)
            fragments.pop(i)
            fragments.append(merged)
    print fragments[0]

f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        concat(one)
f.close()

