
def getDigits(i):
	digits = []
	while i!=0:
		digits = [i%10] + digits
		i = int(i/10)
	return digits

pairs = []

for n in range(10, 100):
	digitsn = getDigits(n)
	if 0 in digitsn: continue
	for d in range(n+1, 100):
		digitsd = getDigits(d)
		if 0 in digitsd: continue

		for a in digitsn:
			if a in digitsd:
				tmp_digitsn = list(digitsn)
				tmp_digitsd = list(digitsd)
				tmp_digitsn.remove(a)
				tmp_digitsd.remove(a)
				if n/d == tmp_digitsn[0]/tmp_digitsd[0]: 
					pairs.append([n, d])


print(pairs)

numerator = 1
denominator = 1
for pair in pairs:
	numerator *= pair[0]
	denominator *= pair[1]
print(numerator)
print(denominator)

#SOLUTION: 100

