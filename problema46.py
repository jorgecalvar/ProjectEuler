#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import math

def getOddComposites():
	n = 3
	while True:
		if not isPrime(n):
			yield n
		n += 2

def isPrime(n):
	if n==1:
		return False
	if n==2:
		return True
	if n%2==0:
		return False
	for i in range(3, n//2):
		if n%i == 0:
			return False
	return True



def compliesWithRule(n):
	for i in range(n):
		if isPrime(i):
			if (n-i)%2==0:
				if isSquare((n-i)/2):
					return True
	return False


def isSquare(n):
	s = math.sqrt(n)
	if int(s) == s:
		return True
	return False



a = getOddComposites()

for _ in range(100000):

	b = a.__next__()

	if not compliesWithRule(b):

		print(b)
		break	





