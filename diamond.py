def print_diamond(n):
    if n == 1:
        print 1
        return
    maxlen = len(str(n*n))
    gap =  maxlen * ' '
    first = 0
    for i in xrange(2*n-1):
        if i < n:
            first = i*n + 1
            print (abs(i-n)-1)*gap + gap.join(map(lambda x: '{0:{1}}'.format(x, maxlen), xrange(first, i, 1-n)))
        else:
            first += 1
            print (abs(i-n)+1)*gap + gap.join(map(lambda x: '{0:{1}}'.format(x, maxlen), xrange(first, n*(i+2-n)-1, 1-n)))

print_diamond(3)

