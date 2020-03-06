#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed clockwised starting with 1 in the center?.


def nextDirection(d):
	if d == 'x': return '-y'
	if d == '-y': return '-x'
	if d == '-x': return 'y'
	if d == 'y': return 'x'

def nextElement(spiral, x, y, d):
	if d == 'x': x+=1
	if d == '-y': y-=1
	if d == '-x': x-=1
	if d == 'y': y+=1
	return spiral[y][x]


tam = 1001

spiral = []

for i in range(tam):
	fila = []
	for j in range(tam):
		fila.append(0)
	spiral.append(fila)

n=1
x=int(tam/2)
y=int(tam/2)
d='y'
while x<tam:
	spiral[y][x] = n
	if nextElement(spiral, x, y, nextDirection(d)) == 0: d=nextDirection(d)
	if d == 'x': x+=1
	if d == '-y': y-=1
	if d == '-x': x-=1
	if d == 'y': y+=1
	n+=1


#Sumamos diagonales
sum = -1
for i in range(tam):
	sum += spiral[i][i]
	sum += spiral[tam-1-i][i]

print(sum)