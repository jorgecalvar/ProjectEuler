#What is the largest n-digit pandigital prime that exists?

#SLOW PROGRAM

def getDigits(i):
	digits = []
	while i!=0:
		digits = [i%10] + digits
		i = i//10
	return digits

def isPandigital(digits, n):
	return len(digits)==n and all(i+1 in digits for i in range(n))


def isPrime(n):
	if n==1: return False
	if n==2: return True
	if n%2==0: return False
	for i in range(3, n//2, 2):
		if n%i==0: return False
	return True


prime_pandigital = []
for i in range(1, 8000000):
	digits = getDigits(i)
	if isPandigital(digits, len(digits)) and isPrime(i):
		prime_pandigital.append(i)
		print("Found "+str(i))
		print("Largest "+str(max(prime_pandigital)))

print(prime_pandigital)
print(max(prime_pandigital))

#RUN UNTIL 8000000
#LARGEST FOUND: 7652413 -> SOLUTION