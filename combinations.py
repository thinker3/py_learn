

def my_combinations(n, r):
    if n<=0 or r<=0 or r>n:
        return []
    ans = [ [i] for i in xrange(n)]
    if r==1:
        return ans
    k = r-1
    while k:
        k -= 1
        temp = []
        for one in ans: 
            for i in xrange(r-k-1, n):
                if i not in one:
                    two = one[:]
                    two.append(i)
                    temp.append(two)
        ans = temp
    return ans

for one in my_combinations(5, 2):
    print one

