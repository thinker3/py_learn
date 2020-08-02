li = [0, 1, 'a', '', ' ', None]
lit = [_f for _f in li if _f]
print(li)
print(lit)


def my_filter(item):
    if isinstance(item, str):
        return True
    else:
        return False

print()
li = [0, 1, 'a', '', ' ', None]
lit = list(filter(my_filter, li))
print(li)
print(lit)


class Nonsense(object):

    def __init__(self, sense):
        self.sense = sense

    def __repr__(self):
        return repr(self.sense)

li = [
    Nonsense(None),
    Nonsense(0),
    Nonsense([]),
    Nonsense(1),
    Nonsense({}),
    Nonsense('href'),
]
print([x for x in li if x.sense])
