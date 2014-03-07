from sys import argv

'''
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
'''

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']


class Hand(object):

    def __init__(self, cards, name):
        self.cards = cards
        self.name = name
        self.is_flush = False
        suits = map(lambda x: x[1], self.cards)
        if len(set(suits)) == 1:
            self.is_flush = True
        values = map(lambda x: x[0], self.cards)
        values = map(lambda x: VALUES[CARDS.index(x)], values)
        values = sorted(values, key=lambda x: - VALUES.index(x))
        self.values = values
        self.value = ''.join(values)
        self.compared_results()

    def compare(self, a, b):
        return VALUES.index(a) - VALUES.index(b)

    def compared_results(self):
        deltas = []
        for i in range(4):
            res = self.compare(self.values[i], self.values[i + 1])
            deltas.append(res)
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
        return False

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
            self.number = int(''.join(map(str, self.deltas)), 2)
            return self.number == 15
        except:
            self.number = int(''.join(map(
                lambda x: '1' if x > 0 else '0', self.deltas)), 2)
            return False

    def has_3_the_same_value(self):
        flag = self.number in (3, 9, 12)
        if flag:
            i = self.deltas.index(0)
            three = self.values[i]
            self.value = ''.join(
                [one for one in self.values if one != three])
            self.value = three + self.value
        return flag

    def has_2_pairs(self):
        flag = self.number in (5, 6, 10)
        if flag:
            indexes = [i for i, x in enumerate(self.deltas) if x == 0]
            pairs = ''.join([self.values[i] for i in indexes])
            self.value = ''.join(
                [one for one in self.values if one not in pairs])
            self.value = pairs + self.value
        return flag

    def has_1_pair(self):
        flag = self.deltas.count(0) == 1
        if flag:
            i = self.deltas.index(0)
            pair = self.values[i]
            self.values.pop(i)
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
    if len(winners) == 1:
        return winners[0]
    elif len(winners) == 2:
        if winners[0].value != winners[1].value:
            return (winners[0]
                    if winners[0].value > winners[1].value
                    else winners[1])


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
