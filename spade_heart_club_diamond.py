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
        self.compared_results()

    def compare(self, a, b):
        return VALUES.index(a) - VALUES.index(b)

    def compared_results(self):
        deltas= []
        for i in range(4):
            res = self.compare(self.values[i], self.values[i+1])
            deltas.append(res)
        self.deltas = deltas

    def is_flush_and_straight(self):
        return self.is_straight() and self.is_flush

    def is_straight(self):
        try:
            self.number = int(''.join(map(str, self.deltas)), 2)
            return self.number == 15
        except:
            self.number = int(''.join(map(lambda x: '1' if x>0 else '0', self.deltas)), 2)
            return False

    def has_4_the_same_value(self):
        if self.number == 1:
            self.four = self.values[0]
            self.one = self.values[-1]
            return True
        if self.number == 8:
            self.four = self.values[1]
            self.one = self.values[0]
            return True
        return False

    def is_full_house(self):
        return self.number in (2, 4)

    def has_3_the_same_value(self):
        return self.number in (3, 9, 12)

    def has_2_pairs(self):
        flag = self.number in (5, 6, 10)
        if flag:
            i = self.deltas.index(0)
            self.pair = [self.values[i]]
            self.values.pop(i)
            self.values.pop(i)
            self.deltas.pop(i)
            i = self.deltas.index(0)
            self.pair.append(self.values[i])
            self.values.pop(i)
            self.values.pop(i)
        return flag

    def has_1_pair(self):
        flag = self.deltas.count(0) == 1
        if flag:
            i = self.deltas.index(0)
            self.pair = self.values[i]
            self.values.pop(i)
            self.values.pop(i)
        return flag


def get_cards(one):
    cards = one.split()
    left = cards[:5]
    right = cards[5:]
    left = Hand(left, 'left')
    right = Hand(right, 'right')
    return [left, right]

def get_winner(one):
    winners = []
    for i in range(2):
        if one[i].is_flush_and_straight():
            winners.append(one[i])
    if len(winners) == 1:
        return winners[0]
    elif len(winners) == 2:
        if winners[0].values[0] == winners[1].values[0]:
            return None
        else:
            return winners[0] if winners[0].values[0] > winners[1].values[0] else winners[1]

    for x in one:
        if x.has_4_the_same_value():
            winners.append(x)
    if len(winners) == 1:
        return winners[0]
    elif len(winners) == 2:
        if winners[0].four == winners[1].four:
            if winners[0].one == winners[1].one:
                return none
            else:
                return winners[0] if winners[0].one > winners[1].one else winners[1]
        else:
            return winners[0] if winners[0].four > winners[1].four else winners[1]



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









