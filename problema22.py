
def score(name, p):

	score = 0

	for l in name:

		if l == "A": score += 1
		elif l == "B": score += 2
		elif l == "C": score += 3
		elif l == "D": score += 4
		elif l == "E": score += 5
		elif l == "F": score += 6
		elif l == "G": score += 7
		elif l == "H": score += 8
		elif l == "I": score += 9
		elif l == "J": score += 10
		elif l == "K": score += 11
		elif l == "L": score += 12
		elif l == "M": score += 13
		elif l == "N": score += 14
		elif l == "O": score += 15
		elif l == "P": score += 16
		elif l == "Q": score += 17
		elif l == "R": score += 18
		elif l == "S": score += 19
		elif l == "T": score += 20
		elif l == "U": score += 21
		elif l == "V": score += 22
		elif l == "W": score += 23
		elif l == "X": score += 24
		elif l == "Y": score += 25
		elif l == "Z": score += 26
		else: score += 0

	return score * p


file = open("names.txt")

string = file.readlines()

file.close()

names = sorted(str(string[0]).split(","))

solucion = 0

p = 1

for n in names:
	
	solucion += score(n, p)

	p+=1

print(solucion)