
import time

def suma_divisores(n):

	suma = 0

	for i in range(1, n):

		if n%i == 0: suma += i

	return suma


def pares(max):

	L = [suma_divisores(i) for i in range(1, max+1)]

	pares = []

	for i in range(max):

		suma = L[i]

		if i+1 < suma and 1<=suma and suma <= max and L[suma-1] == i+1:

			pares.append([i+1, suma])

	return pares

def sumar_pares(pares):

	return sum([sum(i) for i in pares])




solucion = sumar_pares(pares(10000))


print("La solucion es " + str(solucion))