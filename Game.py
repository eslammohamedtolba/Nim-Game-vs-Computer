
from Player import *
from Piles import *

class Game:
    # initialize first player, piles that will be used in game and GameRunning attribute 
    def __init__(self):
        self.Players = [Player()]
        self.Piles = Piles()
        self.GameRunning = True

    # initialize second player and running game betwen two players 
    def StartGame(self):
        while True:
            anotherPlayer = int(input("Do you want to play with another player(0) or with computer player(1): "))
            if anotherPlayer == 0:
                self.Players.append(Player())
                break
            elif anotherPlayer == 1:
                self.Players.append(ComputerPlayer())
                break
        self.Piles.PrintPiles()
        while self.GameRunning:
            for player in self.Players:
                while True:
                    if type(player) == Player: 
                        print(f"player {player.Name}, enter Pile number from above Piles and number of stones you want to remove from this Pile: ")
                        play = player.play()
                    if type(player) == ComputerPlayer:
                        play = player.play(self.Piles)
                        print(f"computer player chose Pile number {play[0]} and removed form it {play[1]}")

                    # check if the current play is correct by choosing pile exists and remove number of stones available in this pile
                    if self.Piles.UpdatePiles(play[0],play[1]):
                        break
                    self.Piles.PrintPiles()
                
                # check if the current player losed the game
                if self.Piles.isLosing():
                    if player == self.Players[0]:
                        print(f"Player {self.Players[1].Name} won!")
                    else:
                        print(f"Player {self.Players[0].Name} won!")
                    self.GameRunning = False
                    break
                self.Piles.PrintPiles()
