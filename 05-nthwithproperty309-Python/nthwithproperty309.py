# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every
# digit (from 0 to 9) at least once. 309 is the smallest number with this property.
# Write the function nthWithProperty309 that takes a non-negative int n and returns
# the nth number with Property309.

def nthwithproperty309(n):
	# Your code goes here
	if(n == 0):
		return 309
	start = 310
	k = 1
	while(True):
		ans = str(pow(start,5))
		if("0" in ans and "1" in ans and "2" in ans and "3" in ans and "4" in ans and "5" in ans and "6" in ans and "7" in ans and "8" in ans and "9" in ans):
			if(k == n):
				return start
			else:
				k = k + 1
		start = start + 1



	pass


