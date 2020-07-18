# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n
# and returns the nth palindromic Prime, which is a palidrome number such that
# it is also a prime. For example, 313 is a palindrome and it is prime
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2


def isprime(a):
	d=0
	for i in range(1,a+1):
		if(a%i == 0):
			d=d+1
	if(d==2):
		return True
	else:
		return False

def fun_nth_palindromic_prime(n):
	k =2
	l =[2,3,5,7]
	c=0
	ans = 0
	while(True):
		if(len(str(k))>1 and k in l):
			c = c+1
		if(len(str(k))>1 and isprime(k) == True and isprime(int(str(k)[::-1])))	:
			c= c+1
		if(c==n+1):
			ans = k
			break
	return ans


