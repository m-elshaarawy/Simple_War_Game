# War Card Game
This is a simple implementation of the classic "War" card game using Object-Oriented Programming (OOP) principles in Python. The game is played with a standard deck of 52 playing cards, and can be played by two players.

# Rules of the Game
The rules of the "War" card game are simple:

 1-The deck of cards is shuffled and divided equally between two players.
 2-Each player flips over the top card of their deck and places it face-up on the table.
 3-The player with the higher card value wins the round and takes both cards, placing them at the bottom of their deck.
 4-If both players reveal cards with the same value, a "war" is declared, and each player must place three additional cards face-down on the table, followed by a fourth card face-up.
 5-The player with the higher value of the fourth card wins the war and takes all cards on the table. If the fourth card values are also equal, the process continues until one player wins.
 6-The game continues until one player has all the cards in the deck and is declared the winner.
# Running the Program
To run the "War" card game, simply execute the war_game.py file in a Python environment. The program will automatically create a deck of cards, shuffle the deck, and distribute the cards to two players. The game will then proceed according to the rules outlined above.

The program will output the current round number, the cards played by each player, and the winner of each round. When a "war" is declared, the program will also output the additional cards played by each player.

# Dependencies
This implementation of the "War" card game requires no external dependencies beyond Python 3.x.

# Acknowledgements
This implementation of the "War" card game was created by [`Mohamed Elshaarawy`](https://github.com/m-elshaarawy) as a simple demonstration of Object-Oriented Programming principles in Python. The rules of the game are based on the classic "War" card game, which has been a popular game for generations.

# License
This program is licensed under the the [MIT License](https://opensource.org/licenses/MIT). Feel free to use and modify this code for your own purposes.