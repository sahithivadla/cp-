# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	n = str(n)
	if len(n)==1:
		return int(n)
	else:
		d= {}
		for i in n:
			if i not in  d:
				d[i] = 1
			else:
				d[i] =d[i]+1

		maxval = max(d.values())
		l = []
		for i in d :
			if d[i] == maxval :
				l.append(i)
		return int(min(l))




