 


i = 20

tabla = [[1] * (i+1)] * (i + 1)


x = i

while x != 0:

	x -= 1

	y = i

	while y != 0:

		y -= 1

		tabla[x][y] = tabla[x][y + 1] + tabla[x+1][y]



print("El resultado final es: " + str(tabla[0][0]))