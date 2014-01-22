
from sys import argv

def get_min(n,k,a,b,c,r):
    m = [a]
    for i in range(k-1):
        m.append((b * m[i] + c) % r)
    for i in range(n-k):
        j = 0
        while j in m:
            j += 1
        m.append(j)
        m.pop(0)
    print m[-1]

f = open(argv[1], 'r')
for one in f:
    if one != '\n':
        get_min(*map(int, one.split(',')))
f.close()

