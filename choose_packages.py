from sys import argv
import itertools
import re


def prepare(one):
    weight_limit, packages = map(str.strip, one.split(':'))
    weight_limit = float(weight_limit)
    if weight_limit > 100:
        weight_limit = 100
    packages = re.findall(r'\((.+?)\)', packages.replace('$', ''))
    packages = map(lambda x: x.split(','), packages)

    def my_filter(t):
        t = t[0], float(t[1]), float(t[2])
        if t[1] > weight_limit or t[2] > 100:
            return None
        return t

    packages = filter(None, map(my_filter, packages))
    return weight_limit, packages


def choose(weight_limit, packages):
    if not packages:
        return '-'
    temp = None
    n = len(packages)
    for i in xrange(n, 0, -1):
        for one in itertools.combinations(packages, i):
            total_weight = sum([x[1] for x in one])
            if total_weight > weight_limit:
                continue
            total_money = sum([x[2] for x in one])
            if (temp is None or temp[0] < total_money or
                    (temp[0] == total_money and temp[1] > total_weight)):
                temp = [total_money, total_weight, [y[0] for y in one]]
    return ','.join(temp[2])

f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        weight_limit, packages = prepare(one)
        print choose(weight_limit, packages)
f.close()
