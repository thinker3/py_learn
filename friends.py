from sys import argv
from string import letters

cases = []
f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        if one == 'END OF INPUT':
            break
        else:
            cases.append(one)
f.close()

def get_wordlist():
    f = open(argv[1], 'r')
    for one in f:
        one = one.strip()
        if one:
            if one == 'END OF INPUT':
                wordlist = f
                break
    return f

def we_are_friends(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a == len_b:
        diff = 0
        for i in xrange(len_a):
            if a[i] != b[i]:
                diff += 1
        if diff == 1:
            return True
        else:
            return False
    elif len_a - len_b == 1 or len_b - len_a == 1:
        pass
    else:
        return False
    if len_b < len_a:
        m = len_a
        more = a
        less = b
    else:
        m = len_b
        more = b
        less = a
    for i in xrange(m):
        temp = more[:i] + more[i+1:]
        if less == temp:
            return True
    return False

def find_friends(word):
    new_friends = []
    wordlist = get_wordlist()
    for one in wordlist:
        one = one.strip()
        if one not in old_friends and we_are_friends(word, one):
            new_friends.append(one)
            old_friends.append(one)
    wordlist.close()
    return new_friends

def find_all_friends(new_friends):
    while 1:
        temp = []
        for one in new_friends:
            friends = find_friends(one)
            temp.extend(friends)
        if temp:
            new_friends = temp
        else:
            return len(old_friends)

for one in cases:
    old_friends = [one]
    new_friends = find_friends(one)
    print find_all_friends(new_friends)









'''
def find_friends(word):
    new_friends = []
    n = len(word)
    for i in xrange(n):
        one = word[:i] + word[i+1:]
        if one != word and one not in old_friends and one in wordlist:
            old_friends.append(one)
            new_friends.append(one)
        for j in letters[:26]:
            one = word[:i] + j + word[i+1:]
            if one != word and one not in old_friends and one in wordlist:
                old_friends.append(one)
                new_friends.append(one)
        for j in letters[:26]:
            one = word[:i] + j + word[i:]
            if one != word and one not in old_friends and one in wordlist:
                old_friends.append(one)
                new_friends.append(one)
    for j in letters[:26]:
        one = word + j
        if one != word and one not in old_friends and one in wordlist:
            old_friends.append(one)
            new_friends.append(one)
    return new_friends

def find_all_friends():
    new_friends = old_friends[:]
    while 1:
        print old_friends
        temp = []
        for one in new_friends:
            friends = find_friends(one)
            temp.extend(friends)
        if temp:
            new_friends = temp
        else:
            return len(old_friends)

'''

