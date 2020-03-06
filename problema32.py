#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital

def getDigits(i):
	digits = []
	while i!=0:
		digits = [i%10] + digits
		i = int(i/10)
	return digits

def isPandigital(digits, n):
	return len(digits)==n and all(i+1 in digits for i in range(n))

products = []
xandy = []

for x in range(1, 1000000):
	digitsx = getDigits(x)
	if len(digitsx) != len(list(set(digitsx))): continue
	for y in range(1, 1000000):
		digitsy = getDigits(y)
		digits = digitsx+digitsy+getDigits(x*y)
		if len(digits)>9: break
		if len(digits)<9: continue
		if len(digitsy) != len(list(set(digitsy))): continue
		print("Analyzing "+str(x)+" "+str(y))
		if isPandigital(getDigits(x)+getDigits(y)+getDigits(x*y), 9):
			if x*y not in products:
				products.append(x*y)
				xandy.append([x, y])


print(products)
print(xandy)
print(sum(products))

#SOLUTION: 45228