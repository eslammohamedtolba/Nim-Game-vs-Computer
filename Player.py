
class Player:
    def __init__(self):
        # Initialize the Name attribute of the player object by taking input from the user.
        self.Name = input("please enter your name: ")
    
    def play(self):
        # Prompt the user to enter the pile number and number of stones in it.
        NumPile = int(input("please enter Pile number: "))
        NumStones = int(input(f"please enter number of Stones from Pile number {NumPile}: "))
        return [NumPile,NumStones]
    



class ComputerPlayer:
    # Initialize the Name attribute of the computer player object.
    def __init__(self):
        self.Name = "computer player"

    # Check if the game is still running or if a player has won.
    def State(self,Piles,IsComputer):
        if Piles.isLosing():
            if IsComputer==1:
                # winnig for another player
                return -1
            else:
                # winning for computer player
                return 1
            
        # still Game running
        return 0
    
    def ChooseSuit(self,Piles,IsComputer):
        play = [0,0,-2 if IsComputer else 2]
        # Loop through all piles and stones.
        for Indexpile in range(1,(Piles.NumPiles)+1):
            for Numstones in range(1,Piles.piles[Indexpile-1]+1):
                if Piles.UpdatePiles(Indexpile,Numstones):
                    state = self.State(Piles,IsComputer)
                    if state==0: 
                        anotherplayer = self.ChooseSuit(Piles,0 if IsComputer==1 else 1)
                        if IsComputer:
                            if anotherplayer[2]>play[2]:
                                play = [Indexpile,Numstones,anotherplayer[2]]
                        else:
                            if anotherplayer[2]<play[2]:
                                play = [Indexpile,Numstones,anotherplayer[2]]

                    else:
                        if IsComputer:
                            if state>play[2]:
                                play = [Indexpile,Numstones,state]
                        else:
                            if state<play[2]:
                                play = [Indexpile,Numstones,state]
                        

                    Piles.piles[Indexpile-1]+=Numstones
        return play


    # Choose a pile and number of stones to remove from that pile.
    def play(self,Piles):
        [Numpile,NumStones] = self.ChooseSuit(Piles,1)[:2]
        return [Numpile,NumStones]