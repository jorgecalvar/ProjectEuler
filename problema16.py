

numero = 2 ** 1000

i = str(numero)

digitos = []

for a in range(len(i)):

	digitos.append(int(i[a:a+1]))


suma = 0

for a in digitos:

	suma += a


print("La suma es: " + str(suma))