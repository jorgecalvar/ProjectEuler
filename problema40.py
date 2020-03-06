# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def getDigits(n):
	digits = []
	while n!=0:
		digits = [n%10] + digits
		n = n//10
	return digits


digits = []

i=0
while len(digits)<1000000:
	print("Adding "+str(i))
	i+=1
	digits += getDigits(i)

producto=1
for j in range(7):
	producto *= digits[10**j-1]


print(producto)