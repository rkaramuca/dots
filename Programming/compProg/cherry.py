numLocations = int(input())
numTrees = input()
numTrees = numTrees.split()
numTrees = [int(i) for i in numTrees]
cases = int(input())
for i in range( cases ):
	sum = 0
	indices = input()
	indices = indices.split()
	indices = [int(i) for i in indices]
	counter = indices[0] - 1
	while(counter < indices[1]):
		sum += numTrees[counter]
		counter += 1
	print(sum)
