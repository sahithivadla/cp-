# Write the function fun_nth_additive_prime(n) that takes a non-negative int n
# and returns the nth Additive Prime, which is a prime number such that
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def isprime(a):
	d=0
	for i in range(1,a+1):
		if(a%i == 0):
			d=d+1
	if(d==2):
		return True
	else:
		return False

def fun_nth_additive_prime(n):
	k = 2
	l = [2,3,5,7]
	c= 0
	ans = 0
	while(True):
		if(len(str(k))==1 and k in l):
			c=c+1
		if(len(str(k))>1 and isprime(k)==True):
			s = sum(list(map(int,str(k))))
			if(isprime(s)==True):
				c=c+1

		if(c==n+1):
			ans = k
			break

		k=k+1
	return k


	return 1