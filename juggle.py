from sys import argv
import re


class Circuit(object):
    def __init__(self, circuit):
        self.hep = circuit[1:]


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
losers = []


def assign(j):
    p = j.preference.pop(0)
    if p not in groups:
        groups[p] = [j]
    else:
        circuit = groups[p]
        if len(circuit) < group_len:
            circuit.append(j)
        else:
            circuit.append(j)
            circuit.sort(key=lambda j: dot(j.hep, circuits[p].hep))
            loser = circuit.pop(0)
            if not loser.preference:
                losers.append(loser)
            else:
                assign(loser)


circuits = []
circuits_over = False
f = open(argv[1], 'r')
for one in f:
    if one.strip():
        if not circuits_over:
            circuit = map(int, re.findall(r'\d+', one))
            c = Circuit(circuit)
            circuits.append(c)
        else:
            juggler = map(int, re.findall(r'\d+', one))
            j = Juggler(juggler)
            assign(j)
    else:
        circuits_over = True
f.close()

c = groups[wanted]
s = sum(map(lambda j: j.index, c))
print losers
print s
