# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

import itertools

#PROGRAM VERY VERY VERY SLOW / MAKE FOR EFFICIET

n_divisibles = [2,3,5,7,11,13,17]



def getDigits(n):
	digits = []
	while n!=0:
		digits = [n%10] + digits
		n = n//10
	return digits

def verifyProperty(digits):
	return all(putDigitsTogether(digits[1+i:4+i])%n_divisibles[i]==0 for i in range(7))


def putDigitsTogether(digits):
	suma = 0
	l = len(digits)
	for i in range(l):
		suma += digits[l-1-i]*10**i
	return suma

def isPandigital(digits, n):
	return all(i in digits for i in range(n))


numbers = []

for digits in itertools.permutations(getDigits(1234567890), 10):
	print("Analyzing "+str(digits))
	if 0 == digits[0]: continue
	if verifyProperty(digits):
		numbers.append(putDigitsTog
			ether(digits))


print(numbers)
print(sum(numbers))

#NUMBERS: [1430952867, 1460357289, 1406357289, 4130952867, 4160357289, 4106357289]
#SOLUTION: 16695334890