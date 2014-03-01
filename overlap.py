from math import cos, sin, radians, sqrt, acos, degrees
import itertools, re
from sys import argv


arclines = []
index = []

f = open(argv[1], 'r')
for one in f:
    if one.strip():
        i, s = one.split(':')
        index.append(int(i))
        floats = re.findall(r"[-+]?\d*\.\d+|\d+", s)
        a, b, c, d = map(float, floats)
        arclines.append(([a, b], [c, d]))
f.close()

bridges_number = len(arclines)

def get_direction(x):
    return cross(*x)

def two_three(point):
    a, b = map(radians, point)
    return (cos(b), sin(b), sin(a))

def cross(a, b):
    return [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]

def unit(p):
    s = sqrt(sum(map(lambda x: x**2, p)))
    return map(lambda x: x/s, p)

def get_cross_points(x):
    x = map(two_three, x)
    p1 = cross(*x)
    p1 = unit(p1)
    p2 = map(lambda x: -x, p1)
    points = (p1, p2)
    return points

def get_angle(a, b):
    ab = sum(i*j for i, j in zip(a, b))
    mag_a = sqrt(sum(map(lambda x: x**2, a)))
    mag_b = sqrt(sum(map(lambda x: x**2, b)))
    mag_ab = mag_a * mag_b
    angle = ab/mag_ab
    return degrees(acos(angle))

error = 0.001

def is_overlap(m, n):
    p1 = cross(directions[m], directions[n])
    p1 = unit(p1)
    p2 = map(lambda x: -x, p1)
    m12 = get_angle(arclines[m][0], arclines[m][1])
    n12 = get_angle(arclines[n][0], arclines[n][1])

    s1 = get_angle(p1, arclines[m][0]) + get_angle(p1, arclines[m][1])
    s2 = get_angle(p1, arclines[n][0]) + get_angle(p1, arclines[n][1])
    if s1 < m12 + error and s2 < n12 + error:
        return True
    s3 = get_angle(p2, arclines[m][0]) + get_angle(p2, arclines[m][1])
    s4 = get_angle(p2, arclines[n][0]) + get_angle(p2, arclines[n][1])
    if s3 < m12 + error and s4 < n12 + error:
        return True
    return False

arclines = map(lambda x: map(two_three, x), arclines)
directions = map(get_direction, arclines)


points = []
numbers = []
for i, j in itertools.combinations(range(bridges_number), 2):
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
    numbers = filter(lambda x: x!=n, numbers)
    points = filter(lambda p: n not in p, points)
    removed.append(n)

left = filter(lambda x: x not in removed, range(bridges_number))
for i in left:
    print index[i]

















