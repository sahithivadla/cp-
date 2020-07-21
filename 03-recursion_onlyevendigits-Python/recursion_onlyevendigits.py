# Without using iteration and without using strings,
# write the recursive function onlyEvenDigits(L),
# that takes a list L of non-negative integers
# (you may assume that), and returns a new list of
# the same numbers only without their odd digits
# (if that leaves no digits, then replace the number with 0).
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844].
# Also the function returns the empty list if the original list is empty.
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(l):

		return driver(l,len(l),0,[])

def driver(l,n,ind,newl):
	if(ind >= n):
		return newl
	newl.append(string_red(l[ind],len(str(l[ind])),0,""))
	return driver(l,n,ind+1,newl)


def string_red(s,stlen,stind,news):
	if(stind>=stlen):
		return int(news)
	if(int(str(s)[stind])%2 == 0):
		news =news+str(s[stind])

	return string_red(s,stlen,stind+1,news)






