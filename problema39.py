#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#{20,48,52}, {24,45,51}, {30,40,50}
#For which value of p ≤ 1000, is the number of solutions maximised?


#SLOW PROGRAM

def getThirdSide(a, b):
	s = [abs(a-b), abs(b+a)]
	return [min(s), max(s)]

def getTriangles(p):
	triangles = []
	for a in range(p//2):
		for b  in range(a, p//2):
			thirdside = getThirdSide(a, b)
			c = p-a-b
			if c>thirdside[0] and c<thirdside[1] and isRightAngle(a,b,c):
				t = [a, b, c]
				t.sort()
				if t not in triangles: triangles.append(t)
	return triangles


def isRightAngle(a, b, c):
	h = max([a, b, c])
	l = [a, b, c]
	l.remove(h)
	return h**2==l[0]**2+l[1]**2

solutions = []

for i in range(1, 1001):
	print("Analyzing "+str(i))
	solutions.append([i, getTriangles(i)])



c2 = [v[1] for v in solutions]
c2_len = [len(v) for v in c2]
s_c2 = max(c2_len)
print(solutions[c2_len.index(s_c2)][0])


#SOLUTION: 840

