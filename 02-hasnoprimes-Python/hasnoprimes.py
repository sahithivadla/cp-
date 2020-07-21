# Write the function hasnoprimes(L) that takes a 2d list L of integers,
# and returns True if L does not contain any primes, and False otherwise.

def isprime(l):
	c=0
	for i in range(1,l+1):
		if(l%i == 0):
			c=c+1
	if(c == 2):
		return True
	else:
		return False

def fun_hasnoprimes(l):
	for i in range(0,len(l)):
		for j in range(0,len(l[i])):
			if(isprime(l[i][j])== True):
				return False
	return True


