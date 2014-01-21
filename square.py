from sys import argv
import re

false = 'false'
true = 'true'

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
        if dot(ab, ac) == 0 and is_length_equal(ab, ac):
            return true
        else:
            return false
    elif i:
        if dot(ab, ad) == 0 and is_length_equal(ab, ad):
            return true
        else:
            return false

    i = is_equal_or_opposite(ac, bd)
    if i == 1:
        if dot(ab, ac) == 0 and is_length_equal(ab, ac):
            return true
        else:
            return false
    elif i:
        if dot(ad, ac) == 0 and is_length_equal(ad, ac):
            return true
        else:
            return false
    else:
        return false

def get_points(one):
    nums = map(int, re.findall(r'-?\d+', one))
    points= []
    for i in range(4):
        points.append((nums[i*2], nums[i*2+1]))
    return points


f = open(argv[1], 'r')
for one in f.readlines():
    if one not in ['\n']:
        print is_square(*get_points(one))











