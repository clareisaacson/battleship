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

PLAYER1 = 1
PLAYER2 = 2

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

WINDOW = tkinter.Tk()
CANVAS = Canvas(WINDOW, width=WIDTH, height=HEIGHT)
CANVAS.pack()


####### MODEL #######

# creates a 2-dimensional N by N list of 0s
# @return {2D list}
def init_board():
  return [[0] * N for i in range(N)]

# checks that coordinates of ship are within the bounds of the board
# @param ship {list} list of tuple coordinates
# @return {boolean}
def is_ship_on_board(ship):
  for (row,col) in ship:
    if row < 0 or row >= N or col < 0 or col >= N:
      return False
  return True

# checks if the letter (row) of all the coordinates of a ship are the same
# @param ship {list} list of tuple coordinates
# @return {boolean}
def same_row(ship):
  letter = ship[0][0]
  for (row,col) in ship:
    if letter != row:
      return False
  return True

# checks if the number (column) of all the coordinates of a ship are the same
# @param ship {list} list of tuple coordinates
# @return {boolean}
def same_column(ship):
  number = ship[0][1]
  for (row,col) in ship:
    if number != col:
      return False
  return True
  
# checks that ship:
#     - is completely vertical OR completely horizontal
#     - has correct size
#     - is contained within the board
#     - occupies consecutive squares on board
# @param ship {list} list of tuple coordinates
# @param size {int}
# @return {boolean}
def is_valid_ship(ship, size):
  if not (same_row(ship) or same_column(ship)):
    return False
  if size != len(ship):
    return False
  if not is_ship_on_board(ship):
    return False
  ship.sort()
  if (same_row(ship)):
    prev = ship[0][1] - 1
    for (row,col) in ship:
      if prev != col - 1:
        return False
      prev = col
  else:
    prev = ship[0][0] - 1
    for (row,col) in ship:
      if prev != row - 1:
        return False
      prev = row
  return True

  
# checks that all coordinates of a ship are unoccupied
# @params ship {list} list of tuple coordinates
# @params board {2D list}
# @return {boolean}
def is_valid_placement(ship, board):
  for (row,col) in ship:
    if board[row][col] != EMPTY:
      return False
  return True

# updates board by marking all coordinates that the ship occupies
# @param ship {list} list of tuple coordinates
# @param board {2D list}
# @return {None}
def place_ship(ship, board):
  for (row,col) in ship:
    board[row][col] = SHIP
	
# marks hit on board at given coordinate
# @param board {2D list}
# @param row {int}
# @param col {int}
# @return {None}  
def mark_hit(board, row, col):
  board[row][col] = HIT

# marks miss on board at given coordinate
# @param board {2D list}
# @param row {int}
# @param col {int}
# @return {None}  
def mark_miss(board, row, col):
  board[row][col] = MISS

# checks if board at given coordinate is a hit
# @param board {2D list} 
# @param row {int}
# @param col {int}
# @return {boolean}
def is_hit(board, row, col):
  return board[row][col] == SHIP

# checks if board at given coordinate is a miss
# @param board {2D list}
# @param row {int}
# @param col {int}
# @return {boolean}
def is_miss(board, row, col):
  return board[row][col] == EMPTY

# removes location from relevant ship in opponent's dictionary
# @param opponent_dict {dict} opponent's ships
# @param opponent {int} opponent player number either 1 or 2
# @param row {int}
# @param col {int}
# @return {None}
def remove_location(opponent_dict, opponent, row, col):
  for (ship_name, ship) in opponent_dict.items():
    if (row, col) in ship:
      if len(ship) == 1:
        print("YOU SUNK PLAYER {}'S {}".format(opponent, ship_name))
      ship.remove((row,col))
      return None
  print("ERROR: COORDINATE NOT FOUND")

# checks if all the ships in the dictionary are empty
# @param ship_dict {dict}
# @return {boolean}
def all_ships_sunk(ship_dict):
  for (ship_name, ship) in ship_dict.items():
    if len(ship) > 0:
      return False
  return True


####### VIEW #######

# draws guess board
# @param board {2D list} a guess board
# @param start_x {int} pixel x-value at which to start drawing
# @param start_y {int} pixel y-value at which to start drawing
# @return {None}
def draw_guess_board(board, start_x, start_y):
  for row in range(N):
    for col in range(N):
      idx = board[row][col]
      color = ['white','gray27','red','blue']
      CANVAS.create_rectangle(start_x+col*GUESS_BOX_SIZE, start_y+row*GUESS_BOX_SIZE,
                              start_x+(col+1)*GUESS_BOX_SIZE, start_y+(row+1)*GUESS_BOX_SIZE,fill=color[idx],width=2)



# draws play board
# @param board {2D list} a play board
# @param start_x {int} pixel x-value at which to start drawing
# @param start_y {int} pixel y-value at which to start drawing
# @return {None}
def draw_play_board(board, start_x, start_y):
  for row in range(N):
    for col in range(N):
      idx = board[row][col]
      color = ['white','gray27','red','blue']
      CANVAS.create_rectangle(start_x+col*PLAY_BOX_SIZE, start_y+row*PLAY_BOX_SIZE,
                              start_x+(col+1)*PLAY_BOX_SIZE, start_y+(row+1)*PLAY_BOX_SIZE,fill=color[idx],width=2)

# draws coordinates along left and top of board
# @param start_x {int} pixel x-value for the board's left edge
# @param start_y {int} pixel y-value for the board's top edge
# @param box_width {int} width of a single box for the relevant board
#        corresponds to the number of pixels between letters/numbers
# @param font_size {int} size of font letters/numbers will be drawn in
# @return {None} 
def draw_coords(start_x,start_y,box_width,font_size):
  start_x -= box_width/2
  start_y -= box_width/2
  for col in range(N):
    CANVAS.create_text(start_x+box_width*(col+1),start_y,text=str(col),font=('Helvetica',font_size),anchor='center')
  for row in range(N):
    text = chr(row+65)
    CANVAS.create_text(start_x,start_y+box_width*(row+1),text=text,font=('Helvetica',font_size),anchor='center')

# draws list of opponents ships and marks which have been sunk
# @param opponent_dict {dict} opponent's ship dictionary
# @param start_x {int} pixel x-value at which to start drawing
# @param start_y {int} pixel y-value at which to start drawing
# @return {None}
def draw_ships(opponent_dict, start_x, start_y):
  for (ship_name,ship) in opponent_dict.items():
    if ship == []:
      color = "red"
    else:
      color = "white"
    CANVAS.create_oval(start_x,start_y,start_x+CIRCLE_WIDTH,start_y+CIRCLE_WIDTH,fill = color,width = 2)
    CANVAS.create_text(start_x+CIRCLE_WIDTH+5,start_y+CIRCLE_WIDTH/2,text=ship_name+' ('+str(SHIP_SIZES[ship_name])+')',anchor='w')
    start_y += 2*CIRCLE_WIDTH

# draws splash screen between turns, displays hit/miss and next player
# @param player {int} player whose turn is up next - either 1 or 2
# @param hit {boolean} True if the turn just taken resulted in a hit, False if it resulted in a miss
# @return {None}
def draw_splash_screen(player, hit):
  if hit:
    text="HIT!"
  else:
    text="MISS!"
  CANVAS.create_rectangle(0,0,WIDTH,HEIGHT,fill="white")
  CANVAS.create_text(WIDTH/2, HEIGHT/2 - 30, text=text, font=('Helvetica',30), anchor='center')
  CANVAS.create_text(WIDTH/2, HEIGHT/2, text = "PLAYER {} BEGIN TURN".format(player), anchor='center')

# draws entire display: guess board and coordinates,
# play board and coordinates, and ships.
# @param player{int} current player either 1 or 2
# @return {None}
def display_board(player):
  # draw these variables #
  # the following four functions won't be defined until the controller section #
  guess_board = get_player_guess_board(player)
  play_board = get_player_play_board(player)
  opponent_dict = get_player_ships(get_opponent(player))

  CANVAS.delete(tkinter.ALL)

  draw_guess_board(guess_board,LEFT_TOP_MARGIN,LEFT_TOP_MARGIN)
  draw_coords(LEFT_TOP_MARGIN,LEFT_TOP_MARGIN,GUESS_BOX_SIZE,12)
  draw_play_board(play_board,LEFT_TOP_MARGIN+PLAY_BOARD_OFFSET,LEFT_TOP_MARGIN+PLAY_BOARD_OFFSET)
  draw_coords(LEFT_TOP_MARGIN+PLAY_BOARD_OFFSET,LEFT_TOP_MARGIN+PLAY_BOARD_OFFSET,PLAY_BOX_SIZE,20)
  draw_ships(opponent_dict, 40, 80+PLAY_BOARD_OFFSET)
  WINDOW.update()

####### CONTROLLER #######

# initializes global variables: 4 boards and 2 dictionaries
# @return {None}
def init_game():
  global PLAYER1_GUESS_BOARD, PLAYER1_PLAY_BOARD, PLAYER2_GUESS_BOARD, PLAYER2_PLAY_BOARD
  global PLAYER1_SHIPS, PLAYER2_SHIPS
  PLAYER1_GUESS_BOARD = init_board()
  PLAYER2_GUESS_BOARD = init_board()
  PLAYER1_PLAY_BOARD = init_board()
  PLAYER2_PLAY_BOARD = init_board()
  PLAYER1_SHIPS = {}
  PLAYER2_SHIPS = {}

# returns the given player's ship dictionary
# @param player {int} current player either 1 or 2
# @return {dict}
def get_player_ships(player):
  if player == PLAYER1:
    return PLAYER1_SHIPS
  else:
    return PLAYER2_SHIPS

# returns the given player's guess board
# @param player {int} current player either 1 or 2
# @return {2D list}
def get_player_guess_board(player):
  if player == PLAYER1:
    return PLAYER1_GUESS_BOARD
  else:
    return PLAYER2_GUESS_BOARD
  
# returns the given player's play board
# @param player {int} current player either 1 or 2
# @return {2D list}
def get_player_play_board(player):
  if player == PLAYER1:
    return PLAYER1_PLAY_BOARD
  else:
    return PLAYER2_PLAY_BOARD

# returns the number corresponding to the opposite player
# @param player {int} current player either 1 or 2
# @return {int}
def get_opponent(player):
  return player % 2 + 1
  
# checks if the input from the user is valid for a ship:
#   - length of each string in the input is 2
#   - first element of each is a letter 'A' through 'J'
#   - second element of each is a number 0 through 9
#   - input_list is not empty
# @param input_list {list} list of strings
# @return {boolean}
def is_valid_ship_input(input_list):
  if input_list == []:
    return False
  for elem in input_list:
    if not ((len(elem) == 2) and 
            (65<=ord(elem[0]) and ord(elem[0])<=64+N) and
            (48<=ord(elem[1]) and ord(elem[1])<=57)):
      return False
  return True

# converts input from list of strings into list of integer tuple coordinate pairs
# @param input_list {list} list of strings
# @return {list} list of coordinate tuples (consistent with model ship representation) 
def convert_input(input_list):
  result = []
  for arg in input_list:
    curr = (ord(arg[0])-65, int(arg[1]))
    result.append(curr)
  return result

# runs loop prompting player to input locations for their ships and placing them on their play board
# complete the TO DO sections (loop that checks valid input is implemented for you)
# @param player {int} current player either 1 or 2
# @param board {2D list} current player's play board
# @param ship_dict {dict} current player's ship dictionary
# @return {None}
def pick_ships(player, board, ship_dict):
  # TO DO: Print something to prompt the player here
  print("PLAYER {}, PLACE YOUR SHIPS".format(player)) 
  for (name,size) in SHIP_SIZES.items():
    inp = input("PLACE A SHIP OF SIZE {}: ".format(size))
    input_list = inp.split()
    while not (is_valid_ship_input(input_list) and is_valid_ship(convert_input(input_list),size) and is_valid_placement(convert_input(input_list),board)):
      print("INVALID SHIP, TRY AGAIN")
      inp = input("PLACE A SHIP OF SIZE {}: ".format(size))
      input_list = inp.split()
    ship = convert_input(input_list)
    place_ship(ship, board)
    ship_dict[name] = ship
    display_board(player)
    # TO DO: implement writeup tasks for pick_ships here
  print("ALL SHIPS HAVE BEEN PLACED")

# checks if the input from the user is valid for a target:
#   - length is 2
#   - first element is a letter 'A' through 'J'
#   - second element is a number 0 through 9
# @param move {str} input for a target to hit
# @return {boolean} 
def is_valid_move_input(move):
  return ((len(move) == 2) and
          (65<=ord(move[0]) and (ord(move[0])<=64+N)) and
          (48<=ord(move[1]) and ord(move[1])<=57))

# checks if a move is valid for the given board
# @param board {2D list} current player's guess board
# @param row {int} 
# @param col {int}
# @return {boolean}
def is_valid_move(board, row, col):
  return board[row][col] == EMPTY

# checks if all of either player's ships are sunk
# @return {boolean}
def is_end_game():
  if all_ships_sunk(get_player_ships(1)):
    print("PLAYER 2 HAS SUNK ALL OF PLAYER 1'S BATTLESHIPS")
    return True
  elif all_ships_sunk(get_player_ships(2)):
    print("PLAYER 1 HAS SUNK ALL OF PLAYER 2'S BATTLESHIPS")
    return True
  else:
    return False

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
  init_game()
  display_board(PLAYER1)
  pick_ships(PLAYER1,get_player_play_board(PLAYER1),PLAYER1_SHIPS)
  display_board(PLAYER2)
  pick_ships(PLAYER2,get_player_play_board(PLAYER2),PLAYER2_SHIPS)
  player = PLAYER1
  while not is_end_game():
    display_board(player)
    # Loop for continually getting move from a a player until valid. Do not change these 4 lines:
    move = input("PLAYER {} ENTER A COORDINATE TO STRIKE: ".format(player))
    while not (is_valid_move_input(move) and is_valid_move(get_player_guess_board(player),ord(move[0])-65,int(move[1]))):
      print("INVALID MOVE, TRY AGAIN")
      move = input("PLAYER {} ENTER A COORDINATE TO STRIKE: ".format(player))

    # TO DO: game play loop writeup tasks
    row = ord(move[0])-65
    col = int(move[1])
    hit = is_hit(get_player_play_board(get_opponent(player)),row,col)
    if hit:
      print('HIT!')
      mark_hit(get_player_play_board(get_opponent(player)),row,col)
      mark_hit(get_player_guess_board(player),row,col)
      remove_location(get_player_ships(get_opponent(player)),get_opponent(player),row,col)
    else:
      print('MISS')
      mark_miss(get_player_guess_board(player),row,col)
    player = get_opponent(player)
    draw_splash_screen(player, hit)
    input("PLAYER {}, PRESS ENTER TO CONTINUE".format(player))
  quit_game()

  # TO DO: quit the game once the game play loop has been exited


