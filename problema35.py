#How many circular primes are there below one million?

import math, itertools

def getDigits(i):
	digits = []
	while i!=0:
		digits = [i%10] + digits
		i = int(i/10)
	return digits

def getRotations(digits):
	rotations = [digits]
	for i in range(1, len(digits)):
		r = []
		for j in range(len(digits)):
			r.append(digits[(j+i)%len(digits)])
		rotations.append(r)
	return rotations

def isPrime(n):
	if n==1: return False
	if n==2: return True
	if n%2==0: return False
	for i in range(3, int(n/2), 2):
		if n%i==0: return False
	return True

def putDigitsTogether(digits):
	suma = 0
	l = len(digits)
	for i in range(l):
		suma += digits[i]*10**(l-i-1)
	return suma

circular_primes = [2,3,5,7]

for i in range(11, 1000000, 2):

	digits = getDigits(i)

	b=False
	for d in digits:
		if d%2==0 or d==5:
			b=True
			break
	if b: continue

	if not isPrime(i): continue
	if i in circular_primes: continue

	print("Analyzing "+str(i))

	rotations = [putDigitsTogether(v) for v in getRotations(digits)]
	iscircular = True
	for r in rotations:
		if not isPrime(r):
			iscircular = False
			break
		if r in circular_primes:
			iscircular = True
			break

	if iscircular:
		for r in rotations:
			if r not in circular_primes:
				circular_primes.append(r)


print(circular_primes)
print(len(circular_primes))	
