#BATTLESHIP

import tkinter
from tkinter import Canvas

# N: size of grid side
N = 10

EMPTY = 0
SHIP = 1
HIT = 2
MISS = 3

SHIP_SIZES = {'CARRIER': 5, 'BATTLESHIP': 4, 'CRUISER': 3, 'SUBMARINE': 3, 'DESTROYER': 2}

### GLOBALS FOR THE VIEW ###

# NOTE: These are the view variables used in the view shown in the writeup
#       Change them to fit your display
LEFT_TOP_MARGIN = 40
BOTTOM_RIGHT_MARGIN = 20
GUESS_BOX_SIZE = 20
PLAY_BOARD_OFFSET = GUESS_BOX_SIZE * N
PLAY_BOX_SIZE = 30
WIDTH = BOTTOM_RIGHT_MARGIN + LEFT_TOP_MARGIN + N*GUESS_BOX_SIZE + N*PLAY_BOX_SIZE
HEIGHT = BOTTOM_RIGHT_MARGIN + LEFT_TOP_MARGIN + N*GUESS_BOX_SIZE + N*PLAY_BOX_SIZE
CIRCLE_WIDTH = 20
############################
##### UNCOMMENT THESE LINES WHEN YOU ARE WORKING ON THE VIEW/CONTROLLER #####
##### THESE LINES SHOULD BE COMMENTED WHEN SUBMITTING TO AUTOLAB!!!!!   #####
##### IF THEY ARE NOT COMMENTED OUT, THE AUTOGRADER WILL FAIL           #####
# WINDOW = tkinter.Tk()
# CANVAS = Canvas(WINDOW, width=WIDTH, height=HEIGHT)
# CANVAS.pack()


####### MODEL #######

# creates a 2-dimensional N by N list of 0s
# @return {2D list}
def init_board():
  pass

# checks that coordinates of ship are within the bounds of the board
# @param ship {list} list of tuple coordinates
# @return {boolean}
def is_ship_on_board(ship):
  pass

# checks if the letter (row) of all the coordinates of a ship are the same
# @param ship {list} list of tuple coordinates
# @return {boolean}
def same_row(ship):
  pass

# checks if the number (column) of all the coordinates of a ship are the same
# @param ship {list} list of tuple coordinates
# @return {boolean}
def same_column(ship):
  pass
  
# checks that ship:
#     - is completely vertical OR completely horizontal
#     - has correct size
#     - occupies consecutive squares on board
# @param ship {list} list of tuple coordinates
# @param size {int}
# @return {boolean}
def is_valid_ship(ship, size):
  pass
  
# checks that all coordinates of a ship are unoccupied
# @params ship {list} list of tuple coordinates
# @params board {2D list}
# @return {boolean}
def is_valid_placement(ship, board):
  pass

# updates board by marking all coordinates that the ship occupies
# @param ship {list} list of tuple coordinates
# @param board {2D list}
# @return {None}
def place_ship(ship, board):
  pass  
	
# marks hit on board at given coordinate
# @param board {2D list}
# @param row {int}
# @param col {int}
# @return {None}  
def mark_hit(board, row, col):
  pass

# marks miss on board at given coordinate
# @param board {2D list}
# @param row {int}
# @param col {int}
# @return {None}  
def mark_miss(board, row, col):
  pass

# checks if board at given coordinate is a hit
# @param board {2D list} 
# @param row {int}
# @param col {int}
# @return {boolean}
def is_hit(board, row, col):
  pass

# checks if board at given coordinate is a miss
# @param board {2D list}
# @param row {int}
# @param col {int}
# @return {boolean}
def is_miss(board, row, col):
  pass

# removes location from relevant ship in opponent's dictionary
# @param opponent_dict {dict} opponent's ships
# @param player {int} current player either 1 or 2
# @param row {int}
# @param col {int}
# @return {None}
def remove_location(opponent_dict, opponent, row, col):
  pass

# checks if all the ships in the dictionary are empty
# @param ship_dict {dict}
# @return {boolean}
def all_ships_sunk(ship_dict):
  pass


####### VIEW #######

# draws guess board
# @param board {2D list} a guess board
# @param start_x {int} pixel x-value at which to start drawing
# @param start_y {int} pixel y-value at which to start drawing
# @return {None}
def draw_guess_board(board, start_x, start_y):
  pass

# draws play board
# @param board {2D list} a play board
# @param start_x {int} pixel x-value at which to start drawing
# @param start_y {int} pixel y-value at which to start drawing
# @return {None}
def draw_play_board(board, start_x, start_y):
  pass

# draws coordinates along left and top of board
# @param start_x {int} pixel x-value for the board's left edge
# @param start_y {int} pixel y-value for the board's top edge
# @param box_width {int} width of a single box for the relevant board
#        corresponds to the number of pixels between letters/numbers
# @param font_size {int} size of font letters/numbers will be drawn in
# @return {None} 
def draw_coords(start_x,start_y,box_width,font_size):
  pass

# draws list of opponents ships and marks which have been sunk
# @param opponent_dict {dict} opponent's ship dictionary
# @param start_x {int} pixel x-value at which to start drawing
# @param start_y {int} pixel y-value at which to start drawing
# @return {None}
def draw_ships(opponent_dict, start_x, start_y):
  pass

# draws splash screen between turns, displays hit/miss and next player
# @param player {int} current player either 1 or 2
# @param hit {boolean} True if turn resulted in a hit, False if it resulted in a miss
# @return {None}
def draw_splash_screen(player, hit):
  pass

# draws entire display: guess board and coordinates,
# play board and coordinates, and ships.
# @param player {int} current player either 1 or 2
# @return {None}
def display_board(player):
  # draw these variables #
  # the following three functions won't be defined until the controller section
  guess_board = get_player_guess_board(player)
  play_board = get_player_play_board(player)
  opponent_dict = get_player_ships(get_opponent(player))

  CANVAS.delete(tkinter.ALL) # clears canvas -- DO NOT REMOVE
  # your code here
  WINDOW.update() # DO NOT REMOVE
  pass


####### CONTROLLER #######

# initializes global variables: 4 boards and 2 dictionaries
# @return {None}
def init_game():
  global PLAYER1_GUESS_BOARD, PLAYER1_PLAY_BOARD, PLAYER2_GUESS_BOARD, PLAYER2_PLAY_BOARD
  global PLAYER1_SHIPS, PLAYER2_SHIPS
  # T0 DO: initialize these variables
  pass

# returns the given player's ship dictionary
# @param player {int} current player either 1 or 2
# @return {dict}
def get_player_ships(player):
  pass

# returns the given player's guess board
# @param player {int} current player either 1 or 2
# @return {2D list}
def get_player_guess_board(player):
  pass
  
# returns the given player's play board
# @param player {int} current player either 1 or 2
# @return {2D list}
def get_player_play_board(player):
  pass

# returns the number corresponding to the opposite player
# @param player {int} current player either 1 or 2
# @return {int} opposite player
def get_opponent(player):
  pass
  
# checks if the input from the user is valid for a ship:
#   - length of each string in the input is 2
#   - first element of each is a letter 'A' through 'J'
#   - second element of each is a number 0 through 9
#   - input_list is not empty
# @param input_list {list} list of strings
# @return {boolean}
def is_valid_ship_input(input_list):
  pass

# converts input from list of strings into list of integer tuple coordinate pairs
# @param input_list {list} list of strings
# @return {list} list of coordinate tuples (consistent with model ship representation) 
def convert_input(input_list):
  pass

# runs loop prompting player to input locations for their ships and placing them on their play board
# complete the TO DO sections (loop that checks valid input is implemented for you)
# @param player {int} current player either 1 or 2
# @param board {2D list} current player's play board
# @param ship_dict {dict} current player's ship dictionary
# @return {None}
def pick_ships(player, board, ship_dict):
  print("PLAYER {}, PLACE YOUR SHIPS".format(player))
  for (name,size) in SHIP_SIZES.items():
    inp = input("PLACE A SHIP OF SIZE {}: ".format(size))
    input_list = inp.split()
    while not (is_valid_ship_input(input_list) and is_valid_ship(convert_input(input_list),size) and is_valid_placement(convert_input(input_list),board)):
      print("INVALID SHIP, TRY AGAIN")
      inp = input("PLACE A SHIP OF SIZE {}: ".format(size))
      input_list = inp.split()
    # TO DO: implement writeup tasks for pick_ships here
  print("ALL SHIPS HAVE BEEN PLACED")

# checks if the input from the user is valid for a target:
#   - length is 2
#   - first element is a letter 'A' through 'J'
#   - second element is a number 0 through 9
# @param move {str} input for a target to hit
# @return {boolean} 
def is_valid_move_input(move):
  pass

# checks if a move is valid for the given board
# @param board {2D list} current player's guess board
# @param row {int} 
# @param col {int}
# @return {boolean}
def is_valid_move(board, row, col):
  pass

# checks if all of either player's ships are sunk
# @return {boolean}
def is_end_game():
  pass

# quits the game -- nothing to modify here
def quit_game():
    print("GOODBYE!")
    try: WINDOW.destroy()  
    except: return None
  
# game play loop for entire game 
# complete TO DO sections (loop that checks valid move input is implemented for you)
# @return {None}  
def play_game():
  # TO DO: pre-gameplay loop tasks from writeup
  while True: # remove True and fill in this condition to keep the game running until it's over
    display_board(player)
    # Loop for continually getting move from a a player until valid. Do not change these 4 lines:
    move = input("PLAYER {} ENTER A COORDINATE TO STRIKE: ".format(player))
    while not (is_valid_move_input(move) and is_valid_move(get_player_guess_board(player),ord(move[0])-65,int(move[1]))):
      print("INVALID MOVE, TRY AGAIN")
      move = input("PLAYER {} ENTER A COORDINATE TO STRIKE: ".format(player))

    # TO DO: game play loop writeup tasks

  # TO DO: quit the game once the game play loop has been exited


