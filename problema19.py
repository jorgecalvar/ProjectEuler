

d = 1

m = 1

s = 1

a = 1900

cuenta = 0



def nuevo_dia():

	global d, m, s, a


	if d == 28 and m == 2:

		if a % 4 == 0 and a != 1900:

			d += 1

		else:

			d = 1

			m = 3


	elif d == 29 and m == 2:

		d = 1

		m = 3

	elif d == 30 and (m == 4 or m == 6 or m == 9 or m == 11):

		d = 1

		m += 1


	elif d == 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):

		if m == 12:

			d = 1

			m = 1

			a += 1

		else:

			d = 1

			m += 1

	else:

		d += 1



	if s == 7:

		s = 1

	else:

		s += 1





while True:

	nuevo_dia()

	if d == 1 and s == 7 and a > 1900:

		cuenta += 1

		print (str(d) + "/" + str(m) + "/" + str(a) + " es domingo. Cuenta: " + str(cuenta))

	if d == 31 and m == 12 and a == 2000:

		break


print("En el siglo XX, ha habido " + str(cuenta) + " domingos que han caído en el primer día del mes")



	

