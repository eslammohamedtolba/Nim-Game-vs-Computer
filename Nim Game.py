'''
Nim Game is a mathematical game of strategy in which two players take turns removing objects from distinct heaps or piles. 
On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same pile. 
The game is typically played as a misère game, in which the player to take the last object loses.
The basic rules for this game are as follows: The game starts with a number of piles of stones, and stones in each pile may not be equal. 
The players alternately pick up one or more stones from a single pile. The player to remove the last stone loses
'''

from Game import *

game = Game()
game.StartGame()