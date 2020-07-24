# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a
# number n is a product of x and (x+1).

import math
def ispronic(n):
	a =1
	b =1
	c= -n
	x1 = abs((-b +math.sqrt((b*b) - 4*a*c))//(2*a))
	x2  = abs((-b - math.sqrt((b*b) - 4*a*c))//(2*a))
	if(abs(x1-x2) == 1):
		return True
	return False

def nthpronicnumber(n):
	# Your code goes here

	start = 0
	k =0
	while(True):
		if(ispronic(start)):
			if(k == n):
				return start
			k = k+ 1
		start = start + 1


