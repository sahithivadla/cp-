# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that
# any values that would otherwise produce a consecutive run of k elements are not present.
# For example:
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3])
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3])
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on
# that copy and return it. Instead, you must directly construct the result here.

def lookandsay(a):
	# Your code goes here
	l =[]
	for i in range(0,len(a)):
	    if(i ==0):
	        c=1
	        for j in range(i+1,len(a)):
	            if(a[i]==a[j]):
	                c =c+1
	            else:
	                break
	        l.append((c,a[i]))
	    else:
	        if(a[i]==a[i-1]):
	            continue
	        else:
	            c=0
	            for j in range(i,len(a)):
	                if(a[i]==a[j]):
	                    c =c+1
	                else:
	                  break
	            l.append((c,a[i]))
	return(l)

def shortenlongruns(L, k):
	# Your code goes here

	count = 0
	res =[]
	for t in lookandsay(l):
		if(t[0]>=k):
			res.extend([t[1]]*(k-1))
		else:
			res.append(t[1])

	pass