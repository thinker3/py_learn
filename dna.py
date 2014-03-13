from sys import argv
import operator

'''
CCC CCA CCG CGC GCC TCC
GCAAG GCAAG GCCAG GCGCG GCGCA GCTAA
No match
'''


def get_distance(segment, temp):
    #genes = 'ACGT'
    if segment == temp:
        return 0
    return 0


def get_segments(one):
    ans = []
    segment, m, dna = one.split()
    m = int(m)
    less, more = len(segment), len(dna)
    for i in xrange(more - less + 1):
        temp = dna[i: i + less]
        d = get_distance(segment, temp)
        if d <= m:
            ans.append((d, temp))
    return ans


f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        ans = get_segments(one)
        if ans:
            ans.sort(key=operator.itemgetter(0, 1))
            ans = [x[1] for x in ans]
            print ' '.join(ans)
        else:
            print 'No match'
f.close()
