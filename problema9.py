
def intenta(a, b, c):

	if ((a**2) + (b**2)) == (c**2):

		return True

	else:

		return False


a = 1

b = 2

c = 3


while True:

	while True:

		if a < (b -1):

			a += 1

		elif b < (c - 1):

			b += 1

			a = 1

		else:

			c += 1

			a = 1

			b = 2

		if (a + b + c) == 1000:

			break


	if intenta(a, b, c):

		break



				


print("El valor a es: " + str(a))
print("El valor b es: " + str(b))
print("El valor c es: " + str(c))

print("La multiplicacion es: " + str(a*b*c))

