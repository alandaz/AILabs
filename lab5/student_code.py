import common

#helpful, but not needed
class variables:
	counter=0

def place(sudoku, row, col, num):
	for x in range(0, 9): 
		if sudoku[row][x] == num: 
			return False 
	for y in range(0, 9): 
		if sudoku[x][col] == num: 
			return False
	rows = row - row % 3
	cols = col - col % 3
	for y in range(0, 3): 
		for x in range(0, 3): 
			if sudoku[y + rows][x + cols] == num: 
				return False 
	return True 
	
def sudoku_backtracking(sudoku):
	variables.counter = 0
	#put your code here
	return variables.counter

def sudoku_forwardchecking(sudoku):
	variables.counter = 0
	#put your code here
	return variables.counter
