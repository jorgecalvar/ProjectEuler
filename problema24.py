
from itertools import permutations

solucion = "".join(list(permutations('0123456789'))[1000000-1])

print(solucion)