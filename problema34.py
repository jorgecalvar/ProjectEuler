#Find the sum of all numbers which are equal to the sum of the factorial of their digits. Num Armstrong
import math

def getDigits(i):
	digits = []
	while i!=0:
		digits = [i%10] + digits
		i = int(i/10)
	return digits

def isFactorialSum(i):
	return i==sum([math.factorial(d) for d in getDigits(i)])


nums = []

for i in range(1, 100000):
	if isFactorialSum(i): 
		nums.append(i)
		print(i)

print(nums)
print(sum(nums))

#SOLUTION: 40730 (1 and 2 are not included as they are not a sum). 40730 = 145 + 40585