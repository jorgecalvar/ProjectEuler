#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def dec_to_bin(i):
	return int(bin(i)[2:])

def getDigits(i):
	digits = []
	while i!=0:
		digits = [i%10] + digits
		i = i//10
	return digits

def isPalindromic(i):
	digits = getDigits(i)
	ispalindromic = True
	l = len(digits)
	for j in range(int(l/2)):
		if digits[j] != digits[l-1-j]:
			ispalindromic = False
			break
	return ispalindromic


palindromics = []

for i in range(1, 1000000):
	print("Analyzing "+str(i))
	if isPalindromic(i) and isPalindromic(dec_to_bin(i)):
		palindromics.append(i)

print(palindromics)
print(sum(palindromics))

#SOLUTION: 872187

