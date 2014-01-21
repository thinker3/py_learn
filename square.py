from sys import argv

false = 'false'
true = 'true'
zero = (0, 0)

def subtract(a, b):
    return b[0]-a[0], b[1]-a[1]

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def is_equal_or_opposite(a, b):
    if (a[0]==b[0] and a[1]==b[1]):
        return 1
    if (a[0]==-b[0] and a[1]==-b[1]):
        return -1
    return 0

def is_length_equal(a, b):
    return a[0]*a[0] + a[1]*a[1] == b[0]*b[0] + b[1]*b[1]

def is_square(a, b, c, d):
    ab = subtract(a, b)
    cd = subtract(c, d)
    ac = subtract(a, c)
    bd = subtract(b, d)
    ad = subtract(a, d)
    i = is_equal_or_opposite(ab, cd)
    if i == 1:
        if dot(ab, ac) == 0 and is_length_equal(ab, ac) and ab != zero:
            return true
        else:
            return false
    elif i:
        if dot(ab, ad) == 0 and is_length_equal(ab, ad) and ab != zero:
            return true
        else:
            return false

    i = is_equal_or_opposite(ac, bd)
    if i == 1:
        if dot(ab, ac) == 0 and is_length_equal(ab, ac) and ab != zero:
            return true
        else:
            return false
    elif i:
        if dot(ad, ac) == 0 and is_length_equal(ad, ac) and ad != zero:
            return true
        else:
            return false
    else:
        return false

f = open(argv[1], 'r')
for one in f.readlines():
    if one.strip():
        points = map(eval, one.split(', '))
        print is_square(*points)
f.close()
print


import sys 
cases = open(sys.argv[1], 'r')
for case in cases:
    if case.strip():
        a, b, c, d = map(eval, case.split(', '))
        ab = b[0]-a[0], b[1]-a[1]
        dc = c[0]-d[0], c[1]-d[1]
        ac = c[0]-a[0], c[1]-a[1]
        bc = c[0]-b[0], c[1]-b[1]
        bd = d[0]-b[0], d[1]-b[1]

        cd = d[0]-c[0], d[1]-c[1]
        ad = d[0]-a[0], d[1]-a[1]
        cb = b[0]-c[0], b[1]-c[1]
        zero = (0, 0)
        if ab == dc:
            if ab[0]*bc[0] + ab[1]*bc[1] == 0:
                if ac[0]*bd[0] + ac[1]*bd[1] == 0:
                    if ab == zero:
                        print 'false'
                    else:
                        print 'true'
                    continue
        if ab == cd:
            if ab[0]*ac[0] + ab[1]*ac[1] == 0:
                if ad[0]*bc[0] + ad[1]*bc[1] == 0:
                    if ab == zero:
                        print 'false'
                    else:
                        print 'true'
                    continue
        if ad == cb:
            if ad[0]*ac[0] + ad[1]*ac[1] == 0:
                if ab[0]*dc[0] + ab[1]*dc[1] == 0:
                    if ad == zero:
                        print 'false'
                    else:
                        print 'true'
                    continue
        print 'false'

cases.close()
print


import sys, re 
cases = open(sys.argv[1], 'r')
for case in cases:
    if case != '\n':
        nums = map(int, re.findall(r'\d+', case))
        points= []
        for i in range(4):
            points.append((nums[i*2], nums[i*2+1]))
        a, b, c, d = points
        ab = b[0]-a[0], b[1]-a[1]
        dc = c[0]-d[0], c[1]-d[1]
        ac = c[0]-a[0], c[1]-a[1]
        bc = c[0]-b[0], c[1]-b[1]
        bd = d[0]-b[0], d[1]-b[1]

        cd = d[0]-c[0], d[1]-c[1]
        ad = d[0]-a[0], d[1]-a[1]
        cb = b[0]-c[0], b[1]-c[1]
        if ab == dc:
            if ab[0]*bc[0] + ab[1]*bc[1] == 0:
                if ac[0]*bd[0] + ac[1]*bd[1] == 0:
                    print 'true'
                    continue
        if ab == cd:
            if ab[0]*ac[0] + ab[1]*ac[1] == 0:
                if ad[0]*bc[0] + ad[1]*bc[1] == 0:
                    print 'true'
                    continue
        if ad == cb:
            if ad[0]*ac[0] + ad[1]*ac[1] == 0:
                if ab[0]*dc[0] + ab[1]*dc[1] == 0:
                    print 'true'
                    continue
        print 'false'

cases.close()







