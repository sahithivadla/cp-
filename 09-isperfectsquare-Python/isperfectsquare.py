# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

import math
def isperfectsquare(n):
	# your code goes here
	if(isinstance(n, str) == True):
		if(n.isalpha()==True or n.isalnum()==True):
			return False
		else:
			a = int(n)
			if(a<0 or isinstance(a,int)==False):
				return False
			else:
				if(isinstance(math.sqrt(a),int)==False):
					return False
				else:
					return True


	else:
		a = int(n)
		if(a<0 or isinstance(a,int)==False):
			return False
		else:
			if(isinstance(math.sqrt(a),int)==False):
				return False
			else:
				return True


