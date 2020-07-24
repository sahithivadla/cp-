# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a
# number n is a product of x and (x+1).

import math
def nthpronicnumber(n):
	# Your code goes here
	a =1
	b =1
	c= -n
	x1 = (-b +math.sqrt((b*b) - 4*a*c))//(2*a)

	pass