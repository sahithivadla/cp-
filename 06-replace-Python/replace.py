# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	ind = s1.index(s2)
	res =""
	res = s[0:ind]+s3+s[ind+len(s2):]

	return res

