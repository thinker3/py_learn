from sys import argv

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']


class Hand(object):

    def __init__(self, cards, name):
        self.name = name
        self.is_flush = False
        suits = map(lambda x: x[1], cards)
        if len(set(suits)) == 1:
            self.is_flush = True
        values = map(lambda x: x[0], cards)
        values = map(lambda x: VALUES[CARDS.index(x)], values)
        self.values = sorted(values, key=lambda x: - VALUES.index(x))
        self.value = ''.join(self.values)
        self.compared_results()

    def compare(self, a, b):
        return VALUES.index(a) - VALUES.index(b)

    def compared_results(self):
        deltas = ''
        for i in range(4):
            res = self.compare(self.values[i], self.values[i + 1])
            deltas += str(res)
        self.deltas = deltas

    def is_flush_and_straight(self):
        return self.is_straight() and self.is_flush

    def has_4_the_same_value(self):
        if self.number == 1:
            self.value = self.values[0] + self.values[-1]
            return True
        if self.number == 8:
            self.value = self.values[1] + self.values[0]
            return True

    def is_full_house(self):
        flag = self.number in (2, 4)
        if flag:
            if self.number == 2:
                self.value = self.values[0] + self.values[-1]
            else:
                self.value = self.values[-1] + self.values[0]
        return flag

    def is_straight(self):
        try:
            self.number = int(self.deltas, 2)
            return self.number == 15
        except:
            self.number = int(''.join(map(
                lambda x: '1' if x > '0' else '0', self.deltas)), 2)

    def has_3_the_same_value(self):
        flag = self.number in (3, 9, 12)
        if flag:
            i = self.deltas.index('0')
            three = self.values[i]
            value = ''.join(
                [one for one in self.values if one != three])
            self.value = three + value
        return flag

    def has_2_pairs(self):
        flag = self.number in (5, 6, 10)
        if flag:
            indexes = [i for i, x in enumerate(self.deltas) if x == '0']
            indexes = [i for i in range(5) if i not in indexes]
            self.value = ''.join([self.values[i] for i in indexes])
        return flag

    def has_1_pair(self):
        flag = (self.deltas.count('0') == 1)
        if flag:
            i = self.deltas.index('0')
            pair = self.values.pop(i)
            self.values.pop(i)
            self.value = pair + ''.join(self.values)
        return flag


def get_cards(one):
    cards = one.split()
    left = cards[:5]
    right = cards[5:]
    left = Hand(left, 'left')
    right = Hand(right, 'right')
    return [left, right]


def get_winner_sub(winners):
    n = len(winners)
    if n == 1:
        return winners[0]
    elif n == 2:
        a, b = winners
        if a.value != b.value:
            return a if a.value > b.value else b


def get_winner(one):
    attrs = [
        'is_flush_and_straight',
        'has_4_the_same_value',
        'is_full_house',
        'is_flush',
        'is_straight',
        'has_3_the_same_value',
        'has_2_pairs',
        'has_1_pair',
        'value',
    ]
    winners = []
    for attr in attrs:
        for x in one:
            m = getattr(x, attr)
            if callable(m):
                if m():
                    winners.append(x)
            elif m:
                winners.append(x)
        winner = get_winner_sub(winners)
        if winner:
            return winner


f = open(argv[1], 'r')
for one in f:
    if one.strip():
        two_hands = get_cards(one)
        winner = get_winner(two_hands)
        if winner:
            print winner.name
        else:
            print 'none'
f.close()
