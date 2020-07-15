# Write the function bonusFindIntRoots(a,b,c) that takes
# the int coefficients a, b, c of a quadratic equation of this form:
#      y = ax2 + bx + c
# You are guaranteed the function has 2 real roots, and in fact that
# the roots are all integers. Your function should return these 2 int roots
# in increasing order. How does a function return multiple values? Like so:
# return root1, root2

import cmath
def fun_find_int_roots(a, b, c):
	d = 0
	l=[]
	d = (b**2) -4*a*c
	sol1 = (-b-cmath.sqrt(d))/(2*a)
	sol2 = (-b+cmath.sqrt(d))/(2*a)
	if(str(sol1)[1]=="-"):
		l.append(int(str(sol1)[1]+str(sol1)[2]))
	if(str(sol1)[2]=="-"):
		l.append(int(str(sol2)[1]+str(sol2)[2]))
	if(str(sol1)[1]!="-" and str(sol2)[1]!="-"):
		l.append(int(str(sol1)[1]))
		l.append(int(str(sol2)[1]))

	l.sort()
	return l[0],l[1]


	# return 0, 0


