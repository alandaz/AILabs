import common
height = common.constants.MAP_HEIGHT 
width = common.constants.MAP_WIDTH 
def df_search(map):
	found = False
	for row in range(height): 
		for col in range(width): 
			if map[row][col] == 2:
				starty = row
				startx = col
				map[starty][startx] = 4
	stack = [(starty, startx)]
	prev = {}
	while len(stack) != 0:
		last = stack.pop()
		row = last[0]
		col = last[1]
		if map[row][col] == 3:
			while((row, col) != (starty,startx)):
				map[row][col] = 5
				parent = prev[(row,col)]
				row = parent[0] 
				col = parent[1]
			map[row][col] = 5
			found = True
			break
		else:
			map[row][col] = 4
			#[y-1][x]
			#[y][x-1]
			#[y+1][x]
			#[y][x+1]
		if (row - 1 >= 0 and (map[row-1][col] == 0 or map[row-1][col] == 3)):
			stack.append((row-1, col))
			prev[(row-1, col)] = (row,col)
		if (col - 1 >= 0 and (map[row][col-1] == 0 or map[row][col-1] == 3)):
			stack.append((row, col-1))
			prev[(row, col-1)] = (row,col)
		if (row + 1 < height and (map[row+1][col] == 0 or map[row+1][col] == 3)):
			stack.append((row+1,col))
			prev[(row+1, col)] = (row,col)
		if (col + 1 < width and (map[row][col + 1] == 0 or map[row][col + 1] == 3)):
			stack.append((row, col+1))
			prev[(row, col+1)] = (row,col)
	return found	

def bf_search(map):
	found = False
	for row in range(height): 
		for col in range(width): 
			if map[row][col] == 2:
				starty = row
				startx = col
				map[starty][startx] = 4
	queue = [(starty, startx)]
	prev = {}
	while len(queue) != 0:
		last = queue.pop(0)
		row = last[0]
		col = last[1]
		if map[row][col] == 3:
			map[row][col] = 5
			while((row, col) != (starty,startx)):
				map[row][col] = 5
				parent = prev[(row,col)]
				row = parent[0] 
				col = parent[1]
			
			found = True
			map[row][col] = 5
			break
		else:
			map[row][col] = 4
			#[y][x+1]
			#[y+1][x]
			#[y][x-1]
			#[y-1][x]
		if (col + 1 < width and (map[row][col+1] == 0 or map[row][col+1] == 3)):
			queue.append((row,col+1))
			prev[(row, col+1)] = (row,col)
		if (row + 1 < height and (map[row+1][col] == 0 or map[row +1 ][col] == 3)):
			queue.append((row +1 , col))
			prev[(row+1, col)] = (row,col)
		if (col - 1 >= 0 and (map[row][col-1] == 0 or map[row][col-1] == 3)):
			queue.append((row, col - 1))
			prev[(row, col - 1)] = (row,col)
		if (row - 1 >= 0 and (map[row -1][col] == 0 or map[row-1][col] == 3)):
			queue.append((row - 1, col))
			prev[(row -1, col)] = (row,col)
		
		
	return found	