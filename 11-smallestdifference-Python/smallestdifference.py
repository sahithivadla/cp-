# Write the function smallestDifference(a) that takes a list of integers and returns
# the smallest absolute difference between any two
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here

	a.sort()
	# return (a[-1]-a[-2])
	m =10000000000000000000000000000
	for i in range(1,len(a)):
		if(a[i]- a[i-1]<m):
			m = a[i]-a[i-1]
		# for j in range(0,len(a)):
		# 	s = a[i]-a[j]
		# 	if(s>0):
		# 		if(s<m):
		# 			m=s
	return m

