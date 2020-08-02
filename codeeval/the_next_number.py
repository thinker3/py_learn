from sys import argv

def get_the_next(one):
    n = len(one)
    for b in range(n-1,0,-1):
        for a in range(b-1,-1,-1):
            if one[a] < one[b]:
                return one[:a] + one[b] + (one[a+1:b] + one[a] + one[b+1:])[::-1]
    return get_next(list(one))

def get_next(left):
    left.reverse()
    n = 0
    while left[0] == '0':
        left.pop(0)
        n += 1
    for i in range(n+1):
        left.insert(1, '0')
    return ''.join(left)

f = open(argv[1], 'r')
for one in f:
    if one.strip():
        try:
            print(get_the_next(one.strip()))
        except:
            print(0) # ???
f.close()
