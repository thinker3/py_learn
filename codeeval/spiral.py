from sys import argv


def spiral_printing(n, m, one):
    if n * m == 1:
        yield one[0]
        return

    def point_2_index(x, y):
        return x * m + y

    ax = 0
    ay = 0
    bx = 0
    by = m - 1
    cx = n - 1
    cy = m - 1
    dx = n - 1
    dy = 0
    while 1:
        for i in xrange(ay, by):
            index = point_2_index(ax, i)
            yield one[index]
        for i in xrange(bx, cx):
            index = point_2_index(i, cy)
            yield one[index]
        for i in xrange(cy, dy, -1):
            index = point_2_index(dx, i)
            yield one[index]
        for i in xrange(dx, ax, -1):
            index = point_2_index(i, ax)
            yield one[index]
        ax += 1
        ay += 1
        bx += 1
        by -= 1
        cx -= 1
        cy -= 1
        dx -= 1
        dy += 1
        if ay > by or ax > dx:
            break
        if ay == by:
            for i in xrange(bx, cx + 1):
                index = point_2_index(i, cy)
                yield one[index]
            break
        elif ax == dx:
            for i in xrange(ay, by + 1):
                index = point_2_index(ax, i)
                yield one[index]
            break

f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        n, m, one = one.split(';')
        n = int(n)
        m = int(m)
        one = one.split(' ')
        print ' '.join(spiral_printing(n, m, one))
f.close()
