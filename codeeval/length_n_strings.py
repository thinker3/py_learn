from sys import argv

def get_strings(n, s):
    letters = set()
    for one in s:
        letters.add(one)
    letters = list(letters)
    return ','.join(power(letters, n))

def power(letters, n):
    ans = letters[:]
    while len(ans[0]) < n:
        temp = []
        for a in ans:
            for b in letters:
                temp.append(a+b)
        ans = temp
    #ans = sorted(ans)
    ans.sort()
    return ans

f = open(argv[1], 'r')
for one in f:
    if one != '\n':
        n, s = one[:-1].split(',')
        n = int(n)
        print get_strings(n, s)
f.close()
