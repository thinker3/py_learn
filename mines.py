from sys import argv

def get_mines(m, n, s):
    for i in range(m*n):
        x = i/n
        y = i%n
        if s[i] == '*':
            yield '*'
        else:
            total = 0
            for a in [x-1, x, x+1]:
                for b in [y-1, y, y+1]:
                    if 0<=a<m and 0<=b<n:
                        if s[a*n + b] == '*':
                            total += 1
            yield str(total)

f = open(argv[1], 'r')
for one in f.readlines():
    if one not in ['\n']:
        mn, s = one.split(';')
        m, n = map(int, mn.split(','))
        print ''.join(get_mines(m, n, s))
f.close()


