from sys import argv

def get_mines(m, n, s):
    mines = []
    for i in range(m*n):
        x = i/n + 1
        y = (i+1)%n
        if not y:
            y = n
        if s[i] == '*':
            mines.append('*')
        else:
            total = 0
            for a in [x-1, x, x+1]:
                for b in [y-1, y, y+1]:
                    if 0<a<=m and 0<b<=n:
                        if s[(a-1)*n + b - 1] == '*':
                            total += 1
            mines.append(str(total))
    return ''.join(mines)

f = open(argv[1], 'r')
for one in f.readlines():
    if one not in ['\n']:
        mn, s = one.split(';')
        m, n = map(int, mn.split(','))
        print get_mines(m, n, s)
f.close()


