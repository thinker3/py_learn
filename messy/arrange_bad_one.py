import random


def factorial(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


def arrange(n):
    aSet = set()
    while len(aSet) < factorial(n):
        l = range(n)
        temp = []
        for i in range(n):
            index = random.randint(0, len(l) - 1)
            temp.append(l.pop(index))
        aSet.add(tuple(temp))
    return aSet


def arrangestr(s):
    n = len(s)
    set_n = arrange(n)
    list_s = s[:]
    temp = []
    for T in set_n:
        #print T
        temp = []
        for j in range(n):
            temp.append(list_s[T[j]])
        print "".join(temp)
    print len(set_n)


arrangestr('abcdefg')
