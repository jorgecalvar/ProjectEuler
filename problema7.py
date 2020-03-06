

cuenta = 1

i = 3

esPrimo = True

solucion = 0

print("Numero primo 1: 2")

while True:

	for b in range (2, i):

		if i%b == 0:

			esPrimo = False

			break


	if esPrimo:

		cuenta = cuenta + 1

		print ("Numero primo " + str(cuenta) + ": " + str(i))

		if cuenta == 10001:

			solucion = i

			break


	esPrimo = True

	i = i + 2


print (str(solucion))

# Posición 6000 - 59359 / Posicion 6239 - 62057