
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
    def __init__(self,hand):
        self.hand=hand

    def __str__(self):
        return f'Contains {len(self.hand)} Cards'     
    
    # Add cards to hand   
    def add(self, added_cards):
        self.hand.extend(added_cards)
    
    # Remove a card from hand 
    def remove_card(self):
        return self.hand.pop(0)


class Player:
    def __init__(self, name, p_hand):
        self.name = name
        self.p_hand = p_hand
    
    # Play a card (remove played card from hand)
    def play_card(self):
        played_card = self.p_hand.remove_card()
        print(f'{self.name} played {played_card}\n')
        return played_card
    
    # Remove war cards 
    def War(self):
        war_cards = []
        if len(self.p_hand.hand) < 3:
            for i in range(len(self.p_hand.hand)):
                war_cards.append(self.p_hand.remove_card())   
        else:
            for i in range(3):
                war_cards.append(self.p_hand.remove_card())
        return war_cards 
    
    # Check if player still has cards 
    def still_have_cards(self):
        return len(self.p_hand.hand) != 0


class Game:
    '''    ''''    '''
    #                #
    #    Game Play   #
    #                #
    '''    ''''    '''
    def __init__(self):
        self.deck=Deck()
        self.deck.shuffle_cards()
        self.c_sets=self.deck.split_in_half()
        self.player1=Player(name=input("Enter player_1's name :"),p_hand=Hand(self.c_sets[0]))
        self.player2=Player(name=input("Enter player_2's name :"),p_hand=Hand(self.c_sets[1]))
        self.table_cards=[]
        self.total_rounds=0
        self.war_count=0
        
    def play_game(self):
        print("Game Started ^_^ ...")
        while self.player1.still_have_cards() and self.player2.still_have_cards():
            self.total_rounds+=1

            p1_card=self.player1.play_card()
            p2_card=self.player2.play_card()
            self.table_cards.append(p1_card)
            self.table_cards.append(p2_card)

            if p1_card.rank == p2_card.rank:
                self.war_count+=1
                print("War! ...")
                self.table_cards.extend(self.player1.War())
                self.table_cards.extend(self.player1.War())

                if RANKS.index(p1_card.rank) < RANKS.index(p2_card.rank):
                    self.player2.p_hand.add(self.table_cards)
                else:
                    self.player1.p_hand.add(self.table_cards)
            else:

                if RANKS.index(p1_card.rank) < RANKS.index(p2_card.rank):
                    self.player2.p_hand.add(self.table_cards)
                else:
                    self.player1.p_hand.add(self.table_cards)

            # check for winner
            if self.player1.still_have_cards() and self.player2.still_have_cards():
                print("Time for new round!")
                print("here are the current standings")
                print(self.player1.name+" has : "+str(len(self.player1.p_hand.hand))+" Cards")
                print(self.player1.name+" has : "+str(len(self.player1.p_hand.hand))+" Cards")
            elif self.player1.still_have_cards() == False:
                print("  ~   Game Over   ~  ")
                print(f'{self.player1.name} wins the game!')
                print("Number of rounds: " + str(self.total_rounds)) 
                print("Number of wars: " + str(self.war_count))
            else:
                print("  ~   Game Over   ~  ")
                print(f'{self.player1.name} wins the game!')
                print("Number of rounds: " + str(self.total_rounds)) 
                print("Number of wars: " + str(self.war_count))

# Game Excute        









        

