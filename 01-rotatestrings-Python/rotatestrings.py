# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k.
# If k is non-negative, the function returns the string s rotated k places to the left.
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	if(n==0):
		return s
	if(n<0):
		if(abs(n)>len(s)):
			n = abs(len(s)+n)
			r = ""
			r = s[n:]+s[0:n]
			return r
		else:
			n = abs(len(s)+n)
			r = ""
			r = s[n:]+s[0:n]
			return r
	if(n>0):
		r =""
		r = s[n:]+s[0:n]
		return r
	return s

