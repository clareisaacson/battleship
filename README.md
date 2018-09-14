# Battleship
Project assignment and implementation in Python 3

### Introduction

This is a project I created as the final project for an introductory computer science course for which I was head teaching assistant. I created the step by step instructions for how the game should be coded, using the MVC (Model, View, Controller) method. 

Included in the repository are:
- A PDF writeup of the project with step by step instructions. (battleship.pdf)
- The starter code containing function stubs that correspond to the instructions (battleship_starter.py)
- A working, playable, solution to the game (battleship_solution.py)
- A file of test functions for the testable functions of the game (test_battleship.py)

### Getting Started

Clone the repository, change into the relevant directory and run the battleship-solution.py file from the command line with Python 3. If implementing the solution, instead open the battleship-starter.py and battleship.pdf files.
```
$ python3 battleship-solution.py
```
A blank Tkinter window will launch at this time. This is where the game board will be displayed.

### Implementation (Optional)

Detailed instructions for programming the game are included in the Battleship PDF which includes instructions for each function. Code should be written in the battleship-starter.py. For simply running and playing the game, skip to the Battleship Overview or Gameplay and Layout sections.

### Battleship Overview

Battleship is a two player game in which players place ships on a grid and take turns guessing at the location of their opponent’s ships. The goal is to be the first player to guess all the locations of each of the opponent’s ships, or to sink each of them. This assignment’s implementation of Battleship has the following rules:
- The game has two 10 x 10 grids, or boards, for each player. The individual squares on the grid are identified by letters (down the left side of the board, corresponding to each row of the grid, A through J), and numbers (across the top of the board, corresponding to each column of the grid, 0 through 9).
- For each player, one of the boards, called the play board, manages the locations of the player’s ships and records the hits they receive from the opposing player. The second board, called the guess board, only records the player’s hits and misses (guesses) on the opponent’s ships. Each player cannot see their opponent’s arrangement of ships.
- Ships are represented as consecutive squares on a board, arranged either horizontally or vertically. Ships cannot overlap on a given board.
- Each player has 5 ships, each of which has a different fixed size, meaning the number of squares occupied. The 5 ships are: Carrier (size 5), Battleship (size 4), Cruiser (size 3), Submarine (size 3), and Destroyer (size 2).
- Before the game starts, each player places their 5 ships on their play board without the opponent’s knowledge of where they are placing them.
- In each turn, the current player picks a target space on the opponent’s board to try and strike one of their ships. The player receives feedback as to whether their guess was a hit or a miss.
- If the player successfully hits one of the opponent’s ships, then in the following turns, the relevant square is colored red on both the player’s guess board and the opponent’s play board.
- Otherwise if the target was a miss, the square will be marked blue only on the player’s guess board, and nothing will change on the opponent’s play board.
- When all squares of a player’s ship have been hit, the ship is sunk. When all the ships of a given player are sunk, the game ends and the opponent wins the game.

### Game Play and Layout

The game is played using the command line with the game state displayed to the player in the Tkinter window. 

The display alternates between Player1 and Player2 with splash screens between turns. The idea behind this is that while the splash screen is up, control of the computer can be given to the next player without them seeing the previous player's layout.

The smaller board in the upper left corner of the window is the "guess board" displaying the current player's guesses and successfull hits on their opponent. The larger board in the lower right corner is the "play board" displaying the current player's own ships and where they have been hit.

### Playing the Game

To start the game call the function play_game.
```
>>> play_game()
```
The game board will appear in the Tkinter window. In the command prompt Player 1 will be prompted to enter coordinates for their first ship of size 5. To do this the player must enter 5 consecutive coordinates (either vertical or horizontally consecutive) in letter,number format separated by a space. Letters must be capital letters.
```
PLACE A SHIP OF SIZE 5: E0 E1 E2 E3 E4
PLACE A SHIP OF SIZE 4: B8 C8 D8 E8
...
```
Player 1 should repeat this for all 5 of their ships with varying sizes. As they are entered they will appear on the play board in grey.

Player 2 will be prompted to do the same thing. When this is done the game will begin.

Player 1 will be prompted to enter a coordiate to strike, followed by enter. A splash screen will be displayed telling the player whether their choice was a hit or a miss, then the next player will be prompted to begin their turn. When a when a while ship is sunk the splash screen will display this.

This continues until one player's ships have all been sunk, at which point the winner will be displayed.

### Testing

An implementation may be tested by playing the game, or by running the tests in the test file. However, these tests in the file are not exhaustive and are intended to be augmented.


