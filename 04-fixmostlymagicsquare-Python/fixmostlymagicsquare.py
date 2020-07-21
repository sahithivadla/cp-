# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic
# square.

from collections import Counter
def fixmostlymagicsquare(L):
	s = []
	for i in range(0,len(L)):
		for j in range(0,len(L[i])):
			s.append(sum(l[i][j]))
	counter  = Counter(s)
	s = s.index(min(counter,key=counter.get))
	a = s.index(min(counter,key=counter.get))
	c = sum(L[a]) - sum(L[a+1])
	d =  L[a][-1]
	L[a][-1] = d - c
	return(L)



	# Your code goes here