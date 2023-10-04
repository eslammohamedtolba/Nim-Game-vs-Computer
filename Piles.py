# Piles class is responsible for initializing the number of piles and the number of stones in each pile
# printing the current state of the piles, updating this piles after each play of both players and check if game is end or not

class Piles:
    # initializes the piles number and stones number in each pile. 
    # It ensures that the number of piles is greater than zero and that each pile has at least one stone.
    def __init__(self):
        while True:
            self.NumPiles = int(input("please enter number of Piles that greater than 0: "))
            if self.NumPiles>0:
                break
        self.piles = []
        for IndexPile in range(self.NumPiles):
            while True:
                self.piles.append(int(input(f"please enter number of stones in Pile number {IndexPile+1}: ")))
                if self.piles[IndexPile]>0:
                    break
                else:
                    self.piles.pop()

    # print the current state of the piles
    def PrintPiles(self):
        print()
        for IndexPile in range(self.NumPiles):
            print(f"  Pile{IndexPile+1} has {{{self.piles[IndexPile]}}}",end = "  ")
        print("\n")
    
    # updates the state of the piles by removing a specified number of stones from a specified pile.
    # It returns True if the update was successful and False otherwise
    def UpdatePiles(self,NumPile,Numstones):
        if NumPile in range(1,self.NumPiles+1):
            if Numstones in range(1,self.piles[NumPile-1]+1):
                self.piles[NumPile-1] -= Numstones
                return True
        return False

    # checks if all the stones have been removed from all the piles, indicating that the game has been lost
    def isLosing(self):
        AllStones = 0
        for pile in self.piles:
            AllStones+=pile
        return AllStones==0
    
