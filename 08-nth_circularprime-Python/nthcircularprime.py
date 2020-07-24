# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth
# Circular prime, which is a prime number that does not contain any 0's and such that all the
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3,
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime,
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def isprime(num):
	c = 0
	for i in range(1,num+1):
		c= c+1
	return(c==2)
def checkCircular(N) :

    #Count digits.
    count = 0
    temp = N
    while (temp > 0) :
        count = count + 1
        temp = temp / 10

    num = N;
    while (isPrime(num)) :

        # Following three lines generate the
        # next circular permutation of a
        # number. We move last digit to
        # first position.
        rem = num % 10
        div = num / 10
        num = (int)((math.pow(10, count - 1))
                                * rem)+ div

        # If all the permutations are checked
        # and we obtain original number exit
        # from loop.
        if (num == N) :
            return True

    return False
def nthcircularprime(n):
# 	# Your code goes here
	l = [2,3,5,7]
	start = 1
	k =0
	while(True):
		if(len(str(start))== 1 and start in l):
			if(k == n):
				return start
			else:
				k = k + 1
		else:
			if(checkCircular(start) == True):
				if(k == n):
					return start
				else:
					k = k + 1




