import common
height = common.constants.MAP_HEIGHT 
width = common.constants.MAP_WIDTH 

def astar_search(map):
	backwards = {}
	forwards = {}
	summation = {}
	
	found = False
	for row in range(height): 
		for col in range(width): 
			if map[row][col] == 2:
				starty = row
				startx = col
				map[starty][startx] = 4
			if map[row][col] ==3: 
				desty = row
				destx = col 
	dist = abs(abs(starty-desty) + abs(startx - destx))
	backwards[(starty, startx)]= 0
	forwards[(starty, startx)]= dist
	summation[(starty, startx)] = 0 + dist

	queue = [(starty, startx)]
	prev = {}
	lst = 0
	while len(queue) != 0:
		bestdistance = 1000000
		bestnode = queue[0]
		lst = 0
		for x, y in enumerate(queue):
			if (summation[y] < bestdistance):
				bestdistance = summation[y]
				bestnode = y
				lst = x
			elif(summation[y] == bestdistance):
				if y[1] < bestnode[1]: 
					bestdistance = summation[y]
					bestnode = y
					lst = x
				elif y[1] == bestnode[1]: 
					if y[0] < bestnode[0]: 
						bestdistance = summation[y]
						bestnode = y
						lst = x	
		last = queue.pop(lst)			
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

		map[row][col] = 4

		if (col + 1 < width and (map[row][col+1] == 0 or map[row][col+1] == 3) and map[row][col+1] not in queue):
			queue.append((row,col+1))
			prev[(row, col+1)] = (row,col)
			forwards[(row, col +1)] = abs(abs(row-desty) + abs((col + 1) - destx))
			backwards[(row, col +1)] = backwards[(row, col)] + 1
			summation[(row, col + 1)] = backwards[(row, col + 1)] + forwards[(row, col + 1)]
		if (row + 1 < height and (map[row+1][col] == 0 or map[row +1 ][col] == 3) and map[row + 1][col] not in queue):
			queue.append((row +1 , col))
			prev[(row+1, col)] = (row,col)
			forwards[(row + 1, col)] = abs(abs((row + 1)-desty) + abs(col - destx))
			backwards[(row + 1, col)] = backwards[(row, col)] + 1
			summation[(row + 1 , col)] = backwards[(row + 1, col)] + forwards[(row + 1, col)]
		if (col - 1 >= 0 and (map[row][col-1] == 0 or map[row][col-1] == 3)and map[row][col-1] not in queue):
			queue.append((row, col - 1))
			prev[(row, col - 1)] = (row,col)
			forwards[(row, col - 1)] = abs(abs(row-desty) + abs((col -1)- destx))
			backwards[(row, col -1)] = backwards[(row, col)] + 1
			summation[(row, col - 1)] = backwards[(row, col - 1)] + forwards[(row, col - 1)]
		if (row - 1 >= 0 and (map[row -1][col] == 0 or map[row-1][col] == 3)and map[row -1][col] not in queue):
			queue.append((row - 1, col))
			prev[(row -1, col)] = (row,col)
			forwards[(row - 1, col)] = abs(abs((row -1)-desty) + abs(col - destx))
			backwards[(row -1, col)] = backwards[(row, col)] + 1
			summation[(row - 1, col)] = backwards[(row -1, col)] + forwards[(row-1, col)]
			
	return found	

