
primes = [2,3]

def chargePrimes():
	global primes
	n=4
	while True:
		prime = True
		for i in primes:
			if n%i==0:
				prime = False
				break
		if prime:
			primes.append(n)
			yield n
		n+=1


for i in chargePrimes():
	print(i)
	if i>1000000:
		break

print(primes)