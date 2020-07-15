# Write the function interleave(s1, s2) that takes two strings, s1 and s2,
# and interleaves their characters starting with the first character in s1.
# For example, interleave('pto', 'yhn') would return the string "python".
# If one string is longer than the other, concatenate the rest of the remaining
# string onto the end of the new string. For example ('a#', 'cD!f2') would return
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	l =0
	bs = ""
	if(s1<s2):
		l=len(s1)
		bs=s2
	elif(s1>s2):
		l =len(s2)
		bs=s1
	else:
		l =s1
	res = ""
	for i in range(0,l):
		res =res + s1[i]+s2[i]
	if(s1!=s2):
		res=res+bs[l:]
	return res



	return ""
