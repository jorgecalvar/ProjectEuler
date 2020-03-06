

a = 0

b = 1

c = 1

suma = 0


while c < 4000000:


	if c % 2 == 0:

		suma += c


	a = b

	b = c

	c = a + b



print(str(suma))