#coding=utf8

import itertools

a = [1, 2]
b = [3, 4, 5]
c = [6, 7, 8, 9]

for one in itertools.product(a, b, c):
    print one
print '*' * 20


def my_product(*args):
    for one in args:
        if any([
            isinstance(one, str),
            isinstance(one, list),
            isinstance(one, tuple),
            isinstance(one, unicode),
        ]) and len(one):
            continue
        else:
            return

    n = len(args)
    tops = map(lambda x: len(x) - 1, args)
    ans = map(lambda x: 0, args)
    yield tuple(args[i][j] for i, j in enumerate(ans))
    while 1:
        for i in reversed(xrange(0, n)):
            if ans[i] != tops[i]:
                ans[i] += 1
                for j in xrange(i + 1, n):
                    ans[j] = 0
                yield tuple(args[i][j] for i, j in enumerate(ans))
                break
        else:
            return


for one in my_product(a, b, c):
    print one
