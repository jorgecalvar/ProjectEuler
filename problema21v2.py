

def suma_divisores(n):

    suma = 0

    for i in range(1, n):

        if n%i == 0: suma += i

    return suma


solucion = 0

for a in range(1, 10000):

    b = suma_divisores(a)

    if a < b and b < 10000 and suma_divisores(b) == a:

        solucion += a

        solucion += b


print(solucion)