from sys import argv
import itertools

divisors = [2, 3, 5, 7]
chars = [',+', ',-', '']


def is_ugly(n):
    for i in divisors:
        if n % i == 0:
            return True


def get_ugly_numbers(one):
    times = 1
    while one.startswith('0'):
        one = one[1:]
        times *= 3
    n = len(one) - 1
    total = 0
    if n < 0:
        return times / 3
    for option in itertools.product(chars, repeat=n):
        option += ('',)
        temp = ''
        for i, j in zip(one, option):
            temp += i + j
        temp = list(map(int, temp.split(',')))
        t = sum(temp)
        if is_ugly(t):
            total += 1
    return total * times

f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        print(get_ugly_numbers(one))
f.close()
