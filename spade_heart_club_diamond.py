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

VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
class Hand(object):
    def __init__(self, cards):
        self.cards = cards
        self.is_flush = False
        self.is_straight = False
        self.is_royal = False
        self.has_4_the_same_value = False
        self.abc()

    def compare(self, a, b):
        return VALUES.index(a) - VALUES.index(b)

    def abc(self):
        suits = map(lambda x: x[1], self.cards)
        if len(set(suits)) == 1:
            self.is_flush = True
        values = map(lambda x: x[0], self.cards)
        values = sorted(values, key=lambda x: VALUES.index(x))
        for i in range(4):
            if self.compare(values[i], values[i+1]) == -1:
                continue
            else:
                if len(set(values)) == 2:
                    self.has_4_the_same_value == True
        else:
            self.is_straight = True
            if values[0] == 'T':
                self.is_royal = True

def get_cards(one):
    cards = one.split()
    left = cards[:5]
    right = cards[5:]
    return left, right

f = open(argv[1], 'r')
for one in f:
    if one.strip():
        left, right = get_cards(one)
        hand_left = Hand(left)
        print hand_left.is_royal
f.close()









