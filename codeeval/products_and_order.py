from sys import argv
import itertools

digits = {
    '0': '0',
    '1': '1',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def order(one):
    one = [digits[i] for i in one]
    for p in itertools.product(*one):
        yield ''.join(p)


f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        print(','.join(order(one)))
f.close()
