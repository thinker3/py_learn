li = ['a', 'b', 'c', 1, 2, 3]
for i, one in enumerate(li):
    print li
    print i, one
    if one == 'b' or one == 2 or one == 3:
        li.pop(i)
        print li


print
li = range(21)
#li = tuple(li) # tuple does not have insert method
for i, one in enumerate(li):
    if i%3 == 2:
        li.insert(i+1, 'a')
print li




print
li = range(21)
#li = tuple(li) # tuple does not have insert method
for i, one in enumerate(li):
    if i%4 == 3:
        li.insert(i, 'a')
li.append('a')
print li
