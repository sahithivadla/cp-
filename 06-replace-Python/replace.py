# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
		x = [i for i in range(len(s1)) if s1.startswith(s2,i)]
		if(len(x)==0):
			return s1
		else:
			print("else")
			while(len(x)==0):
				x = [i for i in range(len(res)) if res.startswith(s2,i)]
				res = res[0:x[0]]+s3+res[x[0]+len(s2):]
			return res



