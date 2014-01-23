
from sys import argv
def multiply(a, b):
    product = []
    for i in a:
        for j in b:
            if isinstance(i, list):
                if i[-1] >= j:
                    continue
                product.append(i+[j])
            else:
                if i >= j:
                    continue
                product.append([i, j])
    return [product]

def get_num(one):
    case, word = one.split(',')
    if not (case and word):
        print 0
        return
    if len(case) < len(word):
        print 0
        return
    if len(case) == len(word):
        if case == word:
            print 1
        else:
            print 0
        return
    occurrences = []
    for ch in word:
        indexes = [i for i, x in enumerate(case) if x == ch]
        occurrences.append(indexes)
    while len(occurrences) >= 2:
        occurrences = multiply(occurrences[0], occurrences[1]) + occurrences[2:]
    print len(occurrences[0])


f = open(argv[1], 'r')
for one in f:
    if one != '\n':
        get_num(one[:-1])
f.close()




