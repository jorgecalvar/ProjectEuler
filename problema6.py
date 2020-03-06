


numero1 = 0

numero2 = 0

for a in range (1, 101):

	numero2 += a

numero2 = numero2 ** 2

for b in range (1, 101):

	numero1 += (b**2)

print (numero2 - numero1)