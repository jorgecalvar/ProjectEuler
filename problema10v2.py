

lista = []

cuenta = 2

suma = 0

for i in range(2000001):

	lista.append(i)

print("Fase uno terminada")


while True:

	if lista[cuenta] != 0:
		
		for a in range(2 * cuenta, 2000001, cuenta):

			lista[a] = 0

		print("Eliminados los multiplos de " + str(cuenta))


	
	if (cuenta**2) > 2000000:

		print("Fase dos terminada")

		break

	else:

		cuenta += 1


for a in lista:

	suma += a



print("La suma final es: " + str(suma - 1)) #Como el algoritmo ha considerado al 1 como primo, hay que eliminarlo
