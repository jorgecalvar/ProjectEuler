#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


serie = 0
for i in range(1, 1001):
	serie += i**i
	serie = serie%10000000000

print(serie)
