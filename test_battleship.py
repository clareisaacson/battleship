############################################################################
# IMPORTANT NOTE                                                                     #
# This test file does very minimal testing of your implementation.         #
# It is up to you to make sure your code is correct.                       #
############################################################################

from pa9_battleship import *

def test_all():
	print('Testing...')
	test_init_board()
	test_is_ship_on_board()
	test_same_row()
	test_same_column()
	test_is_valid_ship()
	test_is_valid_placement()
	test_place_ship()
	test_mark_hit()
	test_mark_miss()
	test_is_hit()
	test_is_miss()
	test_remove_location()
	test_all_ships_sunk()
	print('All tests passed!')

def test_init_board():
	assert(init_board() == 
		[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

def test_is_ship_on_board():
	assert(is_ship_on_board([(1,3), (2, 5), (0, 9)]) == True)

def test_same_row():
	assert(same_row([(1,2), (1,3), (1, 1), (1,5)]) == True)

def test_same_column():
	assert(same_column([(1,3), (2,3), (5,3), (3,3)]) == True)

def test_is_valid_ship():
	assert(is_valid_ship([(4,5),(4,6),(4,7)], 3) == True)

def test_is_valid_placement():
	board = init_board()
	assert(is_valid_placement([(1,4),(2,4),(3,4)], board) == True)

def test_place_ship():
	board = init_board()
	place_ship([(1,3),(2,3),(3,3)], board)
	assert(board == 
		[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

def test_mark_hit():
	board = init_board()

	mark_hit(board, 4, 2)
	assert(board ==
		[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 2, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

def test_mark_miss():
	board = init_board()

	mark_miss(board, 4, 2)
	assert(board ==
		[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 3, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

def test_is_hit():
	assert(is_hit(
		[[3, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
		 [0, 2, 0, 2, 3, 0, 1, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 3, 0, 1, 0, 0, 2, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 1, 0, 2, 0, 0, 0, 0], 
		 [0, 0, 2, 0, 2, 0, 0, 0, 1, 0], 
		 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 2, 0, 0, 0, 0, 2, 0, 3]], 2, 6) == True)

def test_is_miss():
	assert(is_miss(
		[[3, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
		 [0, 2, 0, 2, 3, 0, 1, 0, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 3, 0, 1, 0, 0, 2, 0, 0], 
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 0, 1, 0, 2, 0, 0, 0, 0], 
		 [0, 0, 2, 0, 2, 0, 0, 0, 1, 0], 
		 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
		 [0, 0, 2, 0, 0, 0, 0, 2, 0, 3]], 2, 6) == False)

def test_remove_location():
	opponent_dict = {'CARRIER':[(1,2),(1,3),(1,4),(1,5)], 
			'BATTLESHIP':[(4,2),(3,2),(2,2),(5,2)], 
			'CRUISER':[(8,7),(7,7),(6,7)], 
			'SUBMARINE':[(7,1),(7,2),(7,3)], 
			'DESTROYER':[(7,6),(8,6)]}

	remove_location(opponent_dict, 1, 7, 7)
	assert(opponent_dict == {'CARRIER':[(1,2),(1,3),(1,4),(1,5)], 
			'BATTLESHIP':[(4,2),(3,2),(2,2),(5,2)], 
			'CRUISER':[(8,7),(6,7)], 
			'SUBMARINE':[(7,1),(7,2),(7,3)], 
			'DESTROYER':[(7,6),(8,6)]})

def test_all_ships_sunk():
	assert(all_ships_sunk({'CARRIER':[], 'BATTLESHIP':[], 'CRUISER':[], 
		'SUBMARINE':[], 'DESTROYER':[]}) == True)