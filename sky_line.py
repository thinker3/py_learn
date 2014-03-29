from sys import argv
import ast


def to_list(one):
    return map(ast.literal_eval, one)


def to_points(one):
    points = []
    while one:
        l, h, r = one.pop(0)
        a = (l, h)
        b = (r, h)
        points.append(a)
        points.append(b)
    points.sort(key=lambda x: x[0])
    return points


f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        tuples = to_list(one.split(';'))
        print to_points(tuples)
f.close()
