from enum import Enum

class OrderedEnum(Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __str__(self):
        return '{}'.format(self.name)

class Suit(OrderedEnum):
    Spade   = 0
    Club    = 1
    Heart   = 2
    Diamond = 3

class Rank(OrderedEnum):
    Ace     = 1
    Two     = 2
    Three   = 3
    Four    = 4
    Five    = 5
    Six     = 6
    Seven   = 7
    Eight   = 8
    Nine    = 9
    Ten     = 10
    Jack    = 11
    Queen   = 12
    King    = 13

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{}\t{}".format(self.rank, self.suit)
