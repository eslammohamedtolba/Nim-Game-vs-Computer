# Nim-Game-vs-Computer

This is a Nim game that can be played with another player or with a computer player. 
The game consists of several piles of stones, and the players take turns removing stones from the piles. 
The goal of the game is to avoid taking the last stone in the piles. 
The game is typically played as a misère game, in which the player to take the last stone loses. 

## Player Class
The Player class allows the user to play the game by choosing a pile and number of stones to remove.

## ComputerPlayer Class
The ComputerPlayer class allows the computer to play the game by choosing a best and suit pile and number of stones to remove.

## Game Class
The Game class initializes the Players and Piles attributes and starts the game.
The StartGame method allows the user to choose between playing with another player or with a computer player.
The game continues until one of the players loses.

## Piles Class
The Piles class keeps track of the current state of the piles and updates them based on the moves made by the players. 
The PrintPiles method prints out the current state of the piles. The UpdatePiles method updates the state of the piles based on a given move. 
The isLosing method checks if game end with losing one of the two players that still played last play.

## Contributing
If you find any bugs or issues with this game, please feel free to open an issue on our GitHub repository. 
We also welcome contributions from other developers. If you would like to contribute to this project, please fork our repository and submit a pull request.
