from math import cos, sin, radians, sqrt, acos
import itertools, re
from sys import argv


arclines = []
index = []

f = open(argv[1], 'r')
for one in f:
    if one.strip():
        i, s = one.split(':')
        index.append(int(i))
        floats = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+\.?", s)
        a, b, c, d = list(map(float, floats))
        arclines.append(([a, b], [c, d]))
f.close()

bridges_number = len(arclines)

def get_direction(x):
    return cross(*x)

def two_three(point):
    a, b = list(map(radians, point))
    p = (cos(a)*cos(b), cos(a)*sin(b), sin(a))
    #p = unit((cos(b), sin(b), sin(a)))
    return p

def cross(a, b):
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]

def unit(p):
    s = sqrt(sum([x**2 for x in p]))
    return [x/s for x in p]

def get_angle(a, b):
    ab = sum(i*j for i, j in zip(a, b))
    return acos(ab)

def is_overlap(m, n):
    p1 = cross(directions[m], directions[n])
    p1 = unit(p1)
    p2 = [-x for x in p1]
    m12 = get_angle(arclines[m][0], arclines[m][1])
    n12 = get_angle(arclines[n][0], arclines[n][1])

    m0_p1 = get_angle(p1, arclines[m][0])
    m1_p1 = get_angle(p1, arclines[m][1])
    n0_p1 = get_angle(p1, arclines[n][0])
    n1_p1 = get_angle(p1, arclines[n][1])
    if max(m0_p1, m1_p1) > m12 or max(n0_p1, n1_p1) > n12:
        pass
    else:
        return True

    m0_p2 = get_angle(p2, arclines[m][0])
    m1_p2 = get_angle(p2, arclines[m][1])
    n0_p2 = get_angle(p2, arclines[n][0])
    n1_p2 = get_angle(p2, arclines[n][1])
    if max(m0_p2, m1_p2) > m12 or max(n0_p2, n1_p2) > n12:
        return False
    else:
        return True

arclines = [list(map(two_three, x)) for x in arclines]
directions = list(map(get_direction, arclines))


points = []
numbers = []
for i, j in itertools.combinations(list(range(bridges_number)), 2):
    if is_overlap(i,j):
        points.append((i, j))
        numbers += [i, j]

def get_more(numbers):
    numbers_set = set(numbers)
    d = []
    for one in numbers_set:
        d.append((one, numbers.count(one)))
    d.sort(key = lambda x: -x[1])
    return d.pop(0)[0]

removed = []
while points:
    n = get_more(numbers)
    numbers = [x for x in numbers if x!=n]
    points = [p for p in points if n not in p]
    removed.append(n)

left = [x for x in range(bridges_number) if x not in removed]
for i in left:
    print(index[i])

















