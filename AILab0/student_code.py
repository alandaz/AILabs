def order(data):
	for x in range(1, len(data)): 
		for y in range(0, x): 
			if data[x] < data[y]:
				data.insert(y, data.pop(x))				
	return data
