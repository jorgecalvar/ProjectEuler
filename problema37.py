#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

def isPrime(n):
	if n==1: return False
	if n==2: return True
	if n%2==0: return False
	for i in range(3, n//2, 2):
		if n%i==0: return False
	return True

def getDigits(n):
	digits = []
	while n!=0:
		digits = [n%10] + digits
		n = n//10
	return digits


def getTruncates(n):
	digits = getDigits(n)
	truncates = []
	l = len(digits)
	for i in range(l):
		truncates.append(putDigitsTogether(digits[0:i+1]))
		truncates.append(putDigitsTogether(digits[l-1-i:l]))
	return list(set(truncates))


def putDigitsTogether(digits):
	suma = 0
	l = len(digits)
	for i in range(l):
		suma += digits[l-1-i]*10**i
	return suma


truncatable_primes = []

i=10
while len(truncatable_primes)<11:
	i+=1
	print("Analyzing "+str(i))
	if all(isPrime(v) for v in getTruncates(i)):
		truncatable_primes.append(i)

print(truncatable_primes)
print(sum(truncatable_primes))

#LARGEST TRUNCATABLE PRIME: 739397
#SOLUTION: 748317