#Get the index of the first term in the Fibonnaci sequence with 1000 digits


a = 1
b = 1
c = 2

i = 3

while True:

	a = b

	b = c

	c = a + b

	i += 1


	#We check the number of digits

	number_of_digits = len(str(c))

	print("La posición " + str(i) + " tiene " + str(number_of_digits) + " digitos")

	if(number_of_digits == 1000):
		break


print("La solucion es " + str(i))