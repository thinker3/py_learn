from sys import argv
import itertools
import string

digits_upper_lower_letters = (string.digits +
                              string.uppercase + string.lowercase)


def order(one):
    temp = [digits_upper_lower_letters.index(i) for i in one]
    temp.sort()
    temp = [digits_upper_lower_letters[i] for i in temp]
    for p in itertools.permutations(temp):
        yield ''.join(p)


f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        print(','.join(order(one)))
f.close()
