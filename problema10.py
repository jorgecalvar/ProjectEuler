#Summ all primes below two million

 #We have included 1, 2, 3, 5, 7

suma = 18

primo = True

primos = [3, 5, 7]

i = 11

cuenta = True



while i<2000000:

	for a in primos:

		if (i % a) == 0:

			primo = False

			break


	if primo:

		print("Primo encontrado: " + str(i))

		suma += i

		primos.append(i)

	else:

		primo = True


	if cuenta:

		i += 2

		cuenta = False

	else:

		i += 4

		cuenta = True


print("La suma final es: " + str(suma))