#How many different ways can £2 be made using any number of coins?

#THIS PROGRAM IS VERY VERY SLOW.

def checkCombination(combination, coins, value):
	suma=0
	for i in range(len(combination)):
		suma+=combination[i]*coins[i]
	return suma==value

def difference(combination, coins, value):
	suma=0
	for i in range(len(combination)):
		suma+=combination[i]*coins[i]
	return suma-value

coins = [100, 50, 20, 10, 5, 2, 1]

max_numbers = [2, 4, 10, 20, 40, 100, 200]

combinations = []

value = 200

iterations = 10

combination = list(max_numbers)
while not all(v==0 for v in combination):

	


	print("Analyzing "+str(combination))
	if checkCombination(combination, coins, value):
		combinations.append(combination)

	changes = False
	for i in range(6, -1, -1):
		diff = difference(combination, coins, value)
		if diff > coins[i]:
			diff2 = combination[i]-int(diff/coins[i])
			if diff2 < 0:
				if combination[i]!=0:
					changes = True
					combination[i]=0
			else:
				combination[i] = diff2
				changes = True
				break
			
		else: 
			break
	if changes: continue

	for i in range(6, -1, -1):
		if combination[i] != 0:
			combination[i]-=1
			break
		else:
			combination[i]=max_numbers[i]

	

			
print(len(combinations)+1) #You must sum 1, as the combination of a 2pound coin is not included 

#SOLUTION: 73682

