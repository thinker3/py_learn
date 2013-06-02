import random
li = [int(100*random.random()) for i in xrange(20)]
li = list(set(li))
li.sort()
print li


for i, one in enumerate(li):
    if one<=38 and 38<li[i+1]:
        print one, li[i+1]
        break
