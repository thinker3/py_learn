from sys import argv
import re


class Juggler(object):

    def __init__(self, juggler):
        self.index = juggler[0]
        self.hep = juggler[1:4]
        self.preference = juggler[4:]


def dot(a, b):
    return sum([i * j for i, j in zip(a, b)])


'''
group_len = 6
wanted = 1970
'''
group_len = 4
wanted = 2
groups = {}


def assign(j):
    while 1:
        p = j.preference.pop(0)
        if p not in groups:
            groups[p] = [j]
            break
        else:
            group = groups[p]
            if len(group) < group_len:
                group.append(j)
                break
            else:
                group.append(j)
                loser = min(group, key=lambda j: dot(j.hep, circuits[p]))
                group.remove(loser)
                if loser.preference:
                    j = loser
                else:
                    break


circuits = []
circuits_over = False
f = open(argv[1], 'r')
for one in f:
    if one.strip():
        if not circuits_over:
            circuit = list(map(int, re.findall(r'\d+', one)))[1:]
            circuits.append(circuit)
        else:
            juggler = list(map(int, re.findall(r'\d+', one)))
            j = Juggler(juggler)
            assign(j)
    else:
        circuits_over = True
f.close()

c = groups[wanted]
s = sum([j.index for j in c])
print(s)
