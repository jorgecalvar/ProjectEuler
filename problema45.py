#It can be verified that T285 = P165 = H143 = 40755.
#Find the next triangle number that is also pentagonal and hexagonal.


def getTriangles():
	n = 1
	while True:
		yield n*(n+1)/2
		n += 1

def getPentagonals():
	n = 1
	while True:
		yield n*(3*n-1)/2
		n += 1


def getHexagonals():
	n = 1
	while True:
		yield n*(2*n-1)


def getTriangle(n):
	return n*(n+1)/2

def getPentagonal(n):
	return n*(3*n-1)/2

def getHexagonal(n):
	return n*(2*n-1)





n_t = 286
n_p = 166
n_h = 144

iteraciones = 0


while True:

	iteraciones += 1

	t = getTriangle(n_t)
	p = getPentagonal(n_p)
	h = getHexagonal(n_h)



	if t==p and t==h:
		break

	if t==p and t<h:
		n_t += 1
		n_p += 1
		continue

	if t==p and t>h:
		n_h += 1
		continue

	if t==h and t<p:
		n_t += 1
		n_h += 1
		continue

	if t==h and t>p:
		n_p += 1
		continue

	if p==h and p<t:
		n_p += 1
		n_h += 1
		continue

	if p==h and p>t:
		n_t += 1
		continue


	m = max([t, p, h])

	if t != m:
		n_t += 1
	if p != m:
		n_p += 1
	if h != m:
		n_h += 1





print(f'T({n_t}): {t} / P({n_p}): {p} / H({n_h}): {h}')
print(f'Iteraciones: {iteraciones}')



















