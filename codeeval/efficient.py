from sys import argv
import itertools
import re


def dot(a, b):
    return sum([i * j for i, j in zip(a, b)])


f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        if one.startswith('#'):
            continue
        tankers = list(map(int, re.findall(r'\d+', one)))
        amount = tankers.pop(-1)
        ans = []
        last = tankers.pop(-1)
        max_of_each = [amount / x + 2 for x in tankers]
        vectors = list(map(xrange, max_of_each))
        min_diff = tankers[0] - 1
        for vector in itertools.product(*vectors):
            remainder = (amount - dot(tankers, vector)) % last
            tail = (amount - dot(tankers, vector)) / last
            full_vector = list(vector) + [tail]
            if remainder == 0:
                if tail >= 0:
                    ans.append(full_vector)
            else:
                full_vector[-1] += 1
                diff = dot(tankers + [last], full_vector) - amount
                min_diff = diff if diff < min_diff else min_diff
        ans = list(map(str, ans))
        if ans:
            print(''.join(ans))
        else:
            print(min_diff)
f.close()
