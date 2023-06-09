
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
    def __init__(self):
        print("Created New Orderd Deck")
        self.cards=[card(rank,suite) for suite in SUITES for rank in RANKS]
    
    def shuffle_cards(self):
        print("Shuffling Deck")
        shuffle(self.cards)
        shuffle(self.cards)

    # Crating two card sets out of cards 
    def split_in_half(self):  
        return (self.cards[:len(self.cards)//2],self.cards[len(self.cards)//2:])
    
    

class Hand:
    pass

class Player:
    pass


class game:
    pass

