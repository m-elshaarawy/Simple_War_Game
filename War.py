
from random import shuffle

SUITES=['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS=['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

class card:
    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite
        
    def __str__(self):
        return f'{self.rank} of {self.suite}'

class Deck:
    pass

class Hand:
    pass

class Player:
    pass


class game:
    pass

