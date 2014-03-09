from sys import argv
import re


def is_it_possible(one):
    n, options = one.split(';')
    n = int(n)
    options = options.split('],')
    options = map(lambda x: re.findall(r'\d+', x)[1:], options)
    options.sort(key=len)
    temp = []
    one = options.pop(0)
    if len(one) == n:
        return 'Yes'
    for i in one:
        temp.append([i])
    ans = []
    m = len(options)
    while m > 1:
        option = options.pop(0)
        m = len(options)
        if len(option) == n:
            continue
        for a in temp:
            for b in option:
                if b not in a:
                    c = a + [b]
                    ans.append(c)
        if not ans:
            return 'No'
        else:
            temp = ans
            ans = []
    else:
        if m:
            option = options[0]
            for a in temp:
                for b in option:
                    if b not in a:
                        return 'Yes'
            else:
                return 'No'
        else:
            return 'Yes'

f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        print is_it_possible(one)
f.close()
