from sys import argv

def prepare(one):
    weight_limit, packages = map(str.strip, one.split(':'))
    weight_limit = float(weight_limit)
    if weight_limit > 100:
        weight_limit = 100
    def to_tuple(t):
        try:
            t = t.replace('(', '')
            t = t.replace('$', '')
            t = map(str.strip, t.split(','))
            t = int(t[0]), float(t[1]), float(t[2])
            if t[1] > weight_limit or t[2] > 100:
                return None
            return t
        except:
            return None
    packages = filter(None, map(to_tuple, packages.split(')')))
    packages.sort(key=lambda x: x[1])
    return weight_limit, packages

def handle():
    if not packages:
        return '-'
    temp = None
    n = len(packages)
    for i in range(1, n+1):
        max_of_i_dim = get_max(i, n)
        if not max_of_i_dim:
            break
        if temp is None or temp[0] < max_of_i_dim[0]:
            temp = max_of_i_dim
    return ','.join(map(str, sorted(temp[1])))

import itertools
def get_max(i, n):
    temp = None
    for one in itertools.combinations(packages, i):
        total_weight = 0
        total_money = 0
        for i in one:
            total_weight += i[1]
            total_money += i[2]
        if total_weight > weight_limit:
            continue
        if temp is None or temp[0] < total_money:
            temp = total_money, total_weight, [j[0] for j in one]
        if temp[0] == total_money and temp[1] >= total_weight:
            temp = total_money, total_weight, [j[0] for j in one]
    if temp is None:
        return temp
    return [temp[0], temp[2]]

f = open(argv[1], 'r')
for one in f:
    if one.strip():
        try:
            weight_limit, packages = prepare(one[:-1])
            print handle()
        except:
            print '-'
f.close()
