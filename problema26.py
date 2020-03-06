#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part
import math
from decimal import *



#START PROGRAM
#This program calculates de recurring cycle length of a fraction a/b.
#For the program to work the recurring cycle length must be smaller than (precision-1)/2.

precision = 2000
getcontext().prec = precision

def getRecurringCycleLength(a, b):
	
	f = Decimal(a)/Decimal(b)

	digits = []
	while f!=0:
		f*=10
		digits.append(int(f))
		f-=int(f)

	if len(digits) < precision: return 0 #This means that number is not recurring
	del digits[len(digits)-1] #We delete the last element, for it can be rounded.

	period_start = 0
	while isRecurring(digits)==False:
		del digits[0]
		period_start+=1

	return isRecurring(digits)
	

def isRecurring(digits):
	l=1
	while l<=int(len(digits)/2):
		periodic = True
		exit = False
		for i in range(1, int(len(digits)/l)):
			for j in range(l):
				if digits[j] != digits[i*l+j]:
					periodic = False
					exit = True
					break
			if exit: break
		if periodic:
			return l
		l+=1
	return False

#END PROGRAM

solution = 0
solution_recurring_length = 0

for i in range(1, 1000):
	print("Analyzing "+str(i))
	recurring_length = getRecurringCycleLength(1, i)
	if recurring_length > solution_recurring_length:
		solution = i
		solution_recurring_length = recurring_length



print("Solution " + str(solution))
print("Solution recurring cycle length: "+str(solution_recurring_length))

