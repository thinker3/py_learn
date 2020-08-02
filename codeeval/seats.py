from sys import argv
import re
import itertools


def find_no(m, options):
    for i in range(m, 1, -1):
        for one in itertools.combinations(options, i):
            temp = []
            for j in one:
                for k in j:
                    if k not in temp:
                        temp.append(k)
            yield len(temp) < i


def find_yes(m, options):
    for one in itertools.product(*options):
        s = set(one)
        yield len(s) == m


def is_it_possible(one):
    n, options = one.split(';')
    #n = int(n)
    options = options.split('],')
    options = [re.findall(r'\d+', x)[1:] for x in options]
    m = len(options)

    yes = find_yes(m, options)
    no = find_no(m, options)
    while 1:
        for i in yes:
            if i:
                return 'Yes'
            break
        else:
            return 'No'
        for i in no:
            if i:
                return 'No'
            break
        else:
            return 'Yes'

f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        print(is_it_possible(one))
f.close()
