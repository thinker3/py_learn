from sys import argv

def print_primes(n):
    if n<3:
        return
    temp = [2]
    for i in xrange(3, n, 2):
        print i
        m = i/2
        for j in temp:
            if j > m:
                temp.append(i)
                break
            if i%j != 0:
                continue
            else:
                break
    print ','.join(map(str, temp))
    
f = open(argv[1], 'r')
for one in f:
    if one.strip():
        print_primes(int(one))
f.close()
