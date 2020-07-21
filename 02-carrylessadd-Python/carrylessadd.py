# carry less addition means a  normal addition with the carry from each column ignored.
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	if(x == 0):
		return y
	elif(y ==0):
		return x
	else:
		if(len(str(x)) == len(str(y))):
			res =""
			for i in range(len(str(x))-1,0,-1):
				s = int(str(x)[i]) + int(str(y)[i])
				res=res+str(s)[-i]
			if(res=="00" or res =="000"):
				return int(0)
			else:
				return int(res[::-1])
		else:
			res=""
			s = int(str(x)[-1])+int(str(y)[-1])
			res = res+s[-1]
			res = res+str(x)[0]
			return int(res[::-1])







	return 0

