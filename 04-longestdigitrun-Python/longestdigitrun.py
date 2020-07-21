# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns
# the digit that has the longest consecutive
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's),
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	s = str(abs(n))
	d ={}
	for i in s:
		if i in d:
			d[i]=d[i]+1
		else:
			d[i]=1
	m = max(d.values())
	l = []
	for i in d:
		if(d[i]==m):
			l.append(int(i))
	return min(l)
	pass