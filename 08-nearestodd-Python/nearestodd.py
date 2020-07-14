# Write the function nearestOdd(n) that takes an float n,
# and returns as an int value the nearest odd number to n.
# In the case of a tie, return the smaller odd value.
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.

import numpy as np


def fun_nearestodd(n):
	if(int(n)%2 ==1):
		return int(n)
	elif(".0" in str(n)):
		return int(np.floor(n) // 2 * 2 - 1)
	else:
		a =np.ceil(n) // 2 * 2 + 1
		return (int(a))
		# b = np.floor(n) // 2 * 2 + 1
		# if(b<=a):
		# 	return int(b)
		# else:
		# 	return int(a)


