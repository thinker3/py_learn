import random
li = [int(100*random.random()) for i in xrange(20)]
li = list(set(li))
li.sort()
print li


for i, one in enumerate(li):
    if one<=38 and 38<li[i+1]:
        print one, li[i+1]
        break


def for_for(key=''):
    two_dim = []
    for i in range(5):
        temp = []
        for j in range(100, 103):
            if i == 3:
                two_dim.append([8])
                if key == 'continue':
                    continue
                elif key == 'break':
                    break
                else:
                    pass
            else:
                temp.append(j)
        two_dim.append(temp)
    for one in two_dim:
        print one

print
for_for('continue')
print
for_for('break')
print
for_for()


print
two_dim = []
for i in range(5):
    temp = []
    for j in range(100, 103):
        if i == 3:
            temp.append(8)
            break
        else:
            temp.append(j)
    two_dim.append(temp)
for one in two_dim:
    print one
