
n = 600851475143

primos = []

while n != 1:

	for i in range(2, int(n)+1):

		if n % i == 0:

			print(str(n) + " divido entre " + str(i) + " es " + str(n/i))

			n = n/i

			primos.append(i)

			break


print("El máximo factor primo es " + str(max(primos))

