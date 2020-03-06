#Using words.txt, how many words are triangle words?
#By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.

def isTriangularNumber(a):
	i=1
	while getTriangular(i)<a:
		i+=1
	if getTriangular(i)==a: return True
	return False

def getTriangular(n):
	return int(n*(n+1)/2)


def getWords():
	f = open('words.txt', 'r')
	text = f.read()
	f.close()
	words = []
	for word in text.split(","):
		words.append(word[1:len(word)-1])
	return words

def getWordValue(word):
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	return sum([alphabet.index(v)+1 for v in word])


triangle_words = []

for word in getWords():
	if isTriangularNumber(getWordValue(word)):
		triangle_words.append(word)

print(triangle_words)
print(len(triangle_words))