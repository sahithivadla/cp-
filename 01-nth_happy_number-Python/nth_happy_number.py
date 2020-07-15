# Write the function nthHappyNumber(n) which takes a non-negative integer
# and returns the nth happy number (where the 0th happy number is 1).
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)
def ishappynumber(n):
	n =abs(n)
	if(n == 1):
		return True
	elif(len(str(n))==1):
		n=n*n
		while(n!=1):
			if len(str(n)) == 3 :
				n = int(str(n)[0]) **2 + int(str(n)[1]) **2 + int(str(n)[2]) **2
			elif  len(str(n)) == 2 :
				n = int(str(n)[0]) **2 + int(str(n)[1]) **2

	else:
		while(len(str(n))!=1):
			if len(str(n)) == 3 :
				n = int(str(n)[0]) **2 + int(str(n)[1]) **2 + int(str(n)[2]) **2
			elif  len(str(n)) == 2 :
				n = int(str(n)[0]) **2 + int(str(n)[1]) **2

		if(n==1):
			return True
		return False
def alllist():
	l=[]
	for i in range(0,50):
		if(ishappynumber(i) == True):
			l.append(i)
	return l



def fun_nth_happy_number(n):
	t =[]
	t= alllist()
	return t[n]


