


import sys

numero = 0

naturales = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def comprobarNumero(numero):

	for i in range (100, 999):

		if numero%i == 0:

			if numero/i < 1000:

				print ("Este número divido entre " + str(i) + " es igual a " + str(numero/i))

				sys.exit()

			

	return




for a in naturales:

	numero = 0

	numero += a * 100000 + a

	for b in naturales:

		numero += b * 10000 + b * 10

		for c in naturales:

			numero += c * 1000 + c * 100

			print ("Número generado: " + str(numero))

			#Aquí nuestro numero esta formado y se comprueba si tiene dos divisores de tres cifras

			comprobarNumero(numero)



			numero -= c * 1000 + c * 100


		numero -= b * 10000 + b * 10



