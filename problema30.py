#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def getDigits(i):
	digits = []
	while i!=0:
		digits = [i%10] + digits
		i=int(i/10)
	return digits

def isFifthPower(num):
	suma = 0
	digits = getDigits(num)
	for i in range(len(digits)):
		suma += digits[i]**5
	if suma==num: return True
	return False



	
terms = []

for i in range(1, 200000):
	print("Analyzing "+str(i))
	if isFifthPower(i):
		terms.append(i)

terms.remove(1)

print(terms)
print(sum(terms))