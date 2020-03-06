#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

def getDigits(i):
	digits = []
	while i!=0:
		digits = [i%10] + digits
		i = i//10
	return digits

def isPandigital(digits, n):
	return len(digits)==n and all(i+1 in digits for i in range(n))

def getConcatenatedProduct(i, n):
	digits = []
	for j in range(1, n+1):
		digits += getDigits(j*i)
	return putDigitsTogether(digits)

def putDigitsTogether(digits):
	suma = 0
	l = len(digits)
	for i in range(l):
		suma += digits[l-1-i]*10**i
	return suma

pandigital_products = []

for i in range(1, 10000):
	print("Analyzing "+str(i))
	digits = []
	n=0
	while len(digits)<9:
		n+=1
		digits += getDigits(n*i)
	if len(digits)>9: continue
	if len(digits)!=len(list(set(digits))): continue
	if isPandigital(digits, 9):
		pandigital_products.append([i, n])

print(pandigital_products)

solution_i = max([v[0] for v in pandigital_products])
solution_n = pandigital_products[[v[0] for v in pandigital_products].index(solution_i)][1]

print(getConcatenatedProduct(solution_i, solution_n))

#RUN UNTIL 1000000: LARGEST: 9327
#SOLUTION UNTIL 1000000: [[1, 9], [9, 5], [192, 3], [219, 3], [273, 3], [327, 3], [6729, 2], [6792, 2], [6927, 2], [7269, 2], [7293, 2], [7329, 2], [7692, 2], [7923, 2], [7932, 2], [9267, 2], [9273, 2], [9327, 2]]

#RUN SINCE 1000000 UNTIL 1500000: NONE FOUND
#RUN SINCE 1500000 UNTIL 2000000: NONE FOUND

#SOLUTION: 932718654
