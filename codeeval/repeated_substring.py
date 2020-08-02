from sys import argv

def max_repeated_substring(one):
    one = one[:-1]
    n = len(one)
    ans = ''
    for i in range(n/2, 0, -1):
        for j in range(n-2*i, -1, -1):
            a, b = one[j:j+i], one[j+i:]
            if not a.strip():
                continue
            if a in b:
                ans = a
        if ans:
            return ans

    return 'NONE'

f = open(argv[1], 'r')
for one in f:
    if one != '\n':
        print(max_repeated_substring(one))
f.close()
