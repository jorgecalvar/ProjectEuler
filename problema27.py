#Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

def esPrimo(n):
	if n<0: return False
	if n==1: return False
	if n==2: return True
	if n%2==0: return False
	for i in range(3, n, 2):
		if n%i==0: return False
	return True


def numberOfConsecutivePrimes(a, b):
	n=0
	while esPrimo(evaluate(a, b, n)):
		n+=1
	return n

def evaluate(a, b, n):
	return n**2+a*n+b

sol_a = 0
sol_b = 0
sol_consecutiveprimes = 0

for b in range(1001):
	if not esPrimo(b):
		continue
	for a in range(1, 1000, 2):
		print("Analyzing: "+str(a)+" "+str(b))

		consecutivesprimes = numberOfConsecutivePrimes(a, b)
		if consecutivesprimes > sol_consecutiveprimes:
			sol_a = a
			sol_b = b
			sol_consecutiveprimes = consecutivesprimes

		consecutivesprimes = numberOfConsecutivePrimes(a, -b)
		if consecutivesprimes > sol_consecutiveprimes:
			sol_a = a
			sol_b = -b
			sol_consecutiveprimes = consecutivesprimes

		consecutivesprimes = numberOfConsecutivePrimes(-a, b)
		if consecutivesprimes > sol_consecutiveprimes:
			sol_a = -a
			sol_b = b
			sol_consecutiveprimes = consecutivesprimes

		consecutivesprimes = numberOfConsecutivePrimes(-a, -b)
		if consecutivesprimes > sol_consecutiveprimes:
			sol_a = -a
			sol_b = -b
			sol_consecutiveprimes = consecutivesprimes

print(sol_a)
print(sol_b)
print(sol_consecutiveprimes)

