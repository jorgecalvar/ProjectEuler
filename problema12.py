

def encontrar_numero(limite):

	n = 1

	b = divisores(n)
	c = divisores(n + 1)

	while b * c < 500:

		n += 1

		b = divisores(n)
		c = divisores(n + 1)

		print("El numero " + str(n) + " tiene " + str(b*c) + " divisores")

	return n








def divisores(numero):

	if numero % 2 == 0: 

		numero = numero/2

	divisores = 1

	cuenta = 0

	while numero % 2 == 0:

		cuenta += 1

		numero = numero / 2

	divisores = divisores * (cuenta + 1)

	a = 3

	while numero != 1:

		cuenta = 0

		while numero % a == 0:

			cuenta += 1

			numero = numero / a

		divisores = divisores * (cuenta + 1) 

		a += 2

	return divisores




i = encontrar_numero(500)

resultado = (i * (i + 1)) / 2

print("El resultado final es: " + str(resultado))