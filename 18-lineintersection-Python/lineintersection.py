# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.

import numpy as np

def lineintersection(m1, b1, m2, b2):
	# your code goes here


	A = np.array([[m1, 1], [m2, 1]])
	B = np.array([[b1], [b2]])
	print(np.linalg.inv(A) )


