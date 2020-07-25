# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!")
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally,
# if s does not contain any alphabetic characters, the result should be the empty string ("")


def leastfrequentletters(s):
	# Your code goes here
	s= s.lower()
	d = {}
	for i in s:
	    if(ord(i)>=97 and ord(i)<=122):
    		if i in d:
    			d[i] = d[i]+1
    		else:
    			d[i] = 1
	if(len(d) == 0):
		return ""
	minfreq = min(d.values())
	print(minfreq)
	print(d)
	ans = ""
	for i in d:
	    if(d[i] == minfreq):
	        ans = ans+i
	so = sorted(ans)
	astr= "".join(so)
	return(astr)
