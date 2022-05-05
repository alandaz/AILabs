
QUEENS = 10

def gradient_search(board): 
	initialattacks = attack(board)
	currattacks = initialattacks
	temp = 0 
	initialtempy = 0
	initialtempx = 0

	def set_new_board (board, temploc, initialtempy, initialtempx):
		board[temploc[0]][temploc[1]] = 1
		board[initialtempy][initialtempx] = 0
		return 

	while True: 
		for col in range(10): 
			for row in range(10): 
				if (board[row][col]== 1):
					currqueen = (row, col)
					board[row][col] = 0
					for i in range(QUEENS):
						board[i][col] = 1
						temp = attack(board)
						if (temp < currattacks):
							currattacks = temp
							temploc = [i, col]
							initialtempy = currqueen[0]
							initialtempx = currqueen[1]
						board[i][col] = 0
					board[row][col] = 1
		if currattacks < attack(board):
			set_new_board(board, temploc, initialtempy, initialtempx)
			initialattacks = currattacks

		else:
			return attack(board) == 0
  
def attack(board):
	attacks = 0
	pairs = []
	res = []
	#find all queens and put their coordinates in a list 
	for i in range(10):
		for j in range(10): 
			if board[i][j] == 1:
				pairs.append((i, j))
	for i in range(len(pairs)):
		for j in range(i+1, len(pairs)):
			res.append((pairs[i], pairs[j]))
	for a in res: 
		firstqueen = a[0]
		secondqueen = a[1]
		queen1y = a[0][0]
		queen1x = a[0][1]
		queen2y = a[1][0]
		queen2x = a[1][1]
		if firstqueen[0] == secondqueen[0]: 
			attacks += 1
		queen1y = a[0][0]
		queen1x= a[0][1]
		while queen1y < 10 and queen1x >=0: 
			if queen1y == queen2y and queen1x == queen2x: 
				attacks += 1
			queen1y += 1 
			queen1x -= 1
		queen1y = a[0][0]
		queen1x= a[0][1]
		while queen1y >= 0 and queen1x < 10 : 
			if queen1y == queen2y and queen1x == queen2x: 
				attacks+= 1	
			queen1y -= 1
			queen1x += 1
		queen1y = a[0][0]
		queen1x= a[0][1]
		while queen1y >= 0 and queen1x >=0: 
			if queen1y == queen2y and queen1x == queen2x: 
				attacks += 1
			queen1y -= 1
			queen1x -= 1
		queen1y = a[0][0]
		queen1x= a[0][1]
		while queen1y < 10 and queen1x < 10: 
			if queen1y == queen2y and queen1x == queen2x: 
				attacks += 1
			queen1y += 1
			queen1x += 1
		queen1y = a[0][0]
		queen1x= a[0][1]
	return attacks


		

