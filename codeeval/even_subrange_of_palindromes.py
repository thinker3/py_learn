from sys import argv

def is_palindrome(num):
    if num<10:
        return True
    num = str(num)
    return num == num[::-1]

def is_even(palindromes, r):
    num = 0
    for i in r:
        if i in palindromes:
            num += 1
    return num%2 == 0

def how_many_interesting_subranges(one):
    one = one[:-1]
    left, right = map(int, one.split(' '))
    left_to_right = range(left, right+1)
    n = right+1-left
    palindromes = []
    for i in left_to_right:
        if is_palindrome(i):
            palindromes.append(i)
    total = 0
    for i in xrange(n):
        for j in xrange(i+1, n+1):
            r = left_to_right[i:j]
            if is_even(palindromes, r):
                total += 1
    return total

f = open(argv[1], 'r')
for one in f:
    if one != '\n':
        print how_many_interesting_subranges(one)
f.close()
