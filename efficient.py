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
        tankers = map(int, re.findall(r'\d+', one))
        '''
        import pudb
        pudb.set_trace()
        '''
        amount = tankers.pop(-1)
        ans = []
        remainders = []
        max_of_each = map(lambda x: amount / x + 1, tankers)
        vectors = map(xrange, max_of_each)
        '''
        first = tankers.pop(0)
        for vector in itertools.product(*vectors):
            remainder = (amount - dot(tankers, vector)) % first
            if remainder == 0:
                head = (amount - dot(tankers, vector)) / first
                if head >= 0:
                    ans.append([head] + list(vector))
            else:
                min_remainder.append(remainder)
                #if remainder < min_remainder:
                #    min_remainder = remainder
        '''
        for vector in itertools.product(*vectors):
            remainder = amount - dot(tankers, vector)
            if remainder == 0:
                ans.append(list(vector))
            elif remainder < 0:
                remainders.append(-remainder)
        ans = map(str, ans)
        if ans:
            #ans.sort()
            print ''.join(ans)
        else:
            print min(remainders)
f.close()
