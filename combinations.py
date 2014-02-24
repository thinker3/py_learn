import itertools


def my_combinations(n, r):
    if r>n:
        yield []
        return
    ans = range(r)
    yield ans
    if r<=0:
        return
    while 1:
        for i in xrange(r-1, -1, -1):
            if ans[i] != n-r+i:
                ans = ans[:i] + range(ans[i]+1, ans[i]+1+r-i)
                yield ans
                break
        else:
            return

for one in my_combinations(5, 3):
    print one

print '*' * 20
for one in itertools.combinations(range(5), 3):
    print one
