
def print_primes(n):
    assert n >= 2 and isinstance(n, int)
    temp = [2]
    for i in range(3, n + 1, 2):
        m = i / 2
        for j in temp:
            if j > m:
                temp.append(i)
                break
            if i % j != 0:
                continue
            else:
                break
    for p in temp:
        print(p, end=' ')


class PrimePosition(object):
    def __init__(self, prime, pos):
        self.prime = prime
        self.pos = pos

    def __str__(self):
        return '(%s, %s)' % (self.prime, self.pos)


def new(n):
    assert n >= 2 and isinstance(n, int)
    pp_list = []
    for i in range(2, n + 1):
        j = 0
        for pp in pp_list:
            if pp.pos == i:
                j += 1
                pp.pos += pp.prime
        if j == 0:
            pp_list.append(PrimePosition(i, 2 * i))
    for one in pp_list:
        print(one.prime, end=' ')

print_primes(39)
print()
new(39)
