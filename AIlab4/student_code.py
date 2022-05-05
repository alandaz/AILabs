import common 

def minmax_tictactoe(board, turn):
	winner = 0 
	if turn == 1: 
		winner =  minimaxvalue(board, 1)
	if turn == 2: 
		winner = miniminvalue(board, 2)
	#elif turn == 0: 
	if winner == -1:
		return 2
	elif winner == 1:
		return 1
	elif winner == 0:
		return 0

	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);

	return common.constants.NONE

def minimaxvalue(board, turn):
	status = common.game_status(board)

	count = 0 
	for x in range(0,3): 
		for y in range(0, 3):
			if common.get_cell(board, y, x) == 0:
				count += 1
	if status == 1: 
		return 1
	elif status == 2: 
		return -1
	elif status == 0 and count == 0: 
		return 0 
	
	v = -9999999
	for y in range(0, 3): 
		for x in range(0, 3): 
			if common.get_cell(board, y, x) == 0:
				common.set_cell(board, y, x, 1)
				#value = abprun_tictactoe(board, 'O')
				value = max(v, miniminvalue(board, 2))
				if value > v: 
					v = value
				common.set_cell(board, y, x, 0)
	return v 

def miniminvalue(board, turn):
	status = common.game_status(board)
	count = 0
	for x in range(0,3): 
		for y in range(0, 3):
			if common.get_cell(board, y, x) == 0:
				count += 1
	if status == 1: 
		return 1
	elif status == 2: 
		return -1
	elif status == 0 and count == 0: 
		return 0 

	v =9999999
	for y in range(0, 3):
		for x in range(0,3):
			if common.get_cell(board, y, x) == 0:
				common.set_cell(board, y, x, 2)
				value = min(v, minimaxvalue(board, 1))
				#value = abprun_tictactoe(board, 'X')
				if value < v: 
					v = value
				common.set_cell(board, y, x, 0)
	return v
		

def maxvalue(board, turn, alpha, beta):
	status = common.game_status(board)
	count = 0 
	for x in range(0,3): 
		for y in range(0, 3):
			if common.get_cell(board, y, x) == 0:
				count += 1
	if status == 1: 
		return 1
	elif status== 2: 
		return -1
	elif status == 0 and count == 0: 
		return 0 
	
	v = -999999
	for y in range(0, 3): 
		for x in range(0, 3): 
			if common.get_cell(board, y, x) == 0:
				common.set_cell(board, y, x, 1)
				#value = abprun_tictactoe(board, 'O')
				value = max(v, minvalue(board, 2, alpha, beta))
				if value > v: 
					v = value
				common.set_cell(board, y, x, 0)
				if v >= beta:
					return v 
				if v > alpha: 
					alpha = v
	return v 

def minvalue(board, turn , alpha, beta):
	status = common.game_status(board)
	count = 0
	for x in range(0,3): 
		for y in range(0, 3):
			if common.get_cell(board, y, x) == 0:
				count += 1
	if status == 1: 
		return 1
	elif status == 2: 
		return -1
	elif status == 0 and count == 0: 
		return 0 

	v =99999
	for y in range(0, 3):
		for x in range(0,3):
			if common.get_cell(board, y, x) == 0:
				common.set_cell(board, y, x, 2)
				value = min(v, maxvalue(board, 1, alpha, beta))
				#value = abprun_tictactoe(board, 'X')
				if value < v: 
					v = value
				common.set_cell(board, y, x, 0)
				if v <= alpha:
					return v 
				if v < beta: 
					beta = v
	return v
		
def abprun_tictactoe(board, turn):
	#alpha is max's best option on path to root
	#beta is min's best option on path to root

	winner = 0 
	
	if turn == 1: 
		winner =  maxvalue(board, 1, -float('inf'), float('inf'))
	if turn == 2: 
		winner = minvalue(board, 2, -float('inf'), float('inf'))
	#elif turn == 0: 
	if winner == -1:
		return 2
	elif winner == 1:
		return 1
	elif winner == 0:
		return 0


	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
	
