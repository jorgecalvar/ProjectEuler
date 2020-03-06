#Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

def isPentagonal(i):
	n=1
	while getPentagonal(n)<i:
		n+=1
	if getPentagonal(n)==i: return True
	return False



def getPentagonal(n):
	return int(n*(3*n-1)/2)


def getPentagonals(n1, n2):
	pentagonals = []
	for i in range(n1, n2):
		pentagonals.append(getPentagonal(i))
	return pentagonals


solution = []
solution_d = 10000


n1 = 1

while True:

	pentagonal_n1 = getPentagonal(n1)

	d_next = getPentagonal(n1+1)-pentagonal_n1
	if abs(d_next)>solution_d: break

	n2 = n1+1

	while True:

		print("Analyzing "+str(n1)+" "+str(n2))

		pentagonal_n2 = getPentagonal(n2)

		s = pentagonal_n1+pentagonal_n2
		d = pentagonal_n2-pentagonal_n1
		if isPentagonal(s) and isPentagonal(abs(d)) and abs(d)<solution_d:
			solution = [n1, n2]
			solution_d = abs(d)
		if d<0 and abs(d)>solution_d: break

		n2+=1

	n1+=1



print(solution)
print(solution_d)