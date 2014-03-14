from sys import argv
import operator


def levenshtein(s1, s2):
    '''
    copied from wikibooks
    '''
    if len(s1) < len(s2):
        s1, s2 = s2, s1
        #return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            # j+1 instead of j
            # since previous_row and current_row are one character longer
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def get_segments(one):
    ans = []
    segment, m, dna = one.split()
    m = int(m)
    less, more = len(segment), len(dna)
    for i in xrange(more - less + 1):
        temp = dna[i: i + less]
        d = levenshtein(segment, temp)
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
