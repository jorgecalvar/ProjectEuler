

numero = 1000000

cuenta = 1

resultado = 0

while numero > 100:

	numero -= 1

	i = numero

	cuenta = 0


	while i != 1:

		if i % 2 == 0:

			i = i / 2

		else: 

			i = 3 * i + 1


		cuenta += 1


	if resultado < cuenta:

		resultado = cuenta

		print("La cadena del número " + str(numero) + " tiene " + str(cuenta) + " números")