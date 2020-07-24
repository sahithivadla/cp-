# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth
# Circular prime, which is a prime number that does not contain any 0's and such that all the
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3,
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime,
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
import math
def isprime(num):
	if(num < 2):
		return False
	if(num == 2):
		return True
	if(num%2 ==0):
		return False
	for i in range(3 ,int(math.sqrt(num))+1,2):
		if num%i == 0:
			return False
	return True

def checkCircular(N) :
	if("0" in str(N)):
		return False
	leng = len(str(N))
	if(leng == 1):
		if(isprime(N)):
			return True
		return False
	i = 0
	rem = 0
	while(i<leng):
		rem = N%10
		N = N//10
		N = rem *(10 **(leng -1)) + N
		if not isprime(N):
			return False
		i = i+1
	return True

def nthcircularprime(n):
# 	# Your code goes here
	start = 1
	k =1
	while(True):
		if(checkCircular(start) == True):
			if(k == n):
				return start
			else:
				k = k + 1
		start = start +1




