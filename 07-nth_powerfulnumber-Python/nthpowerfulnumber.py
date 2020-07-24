# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it.
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


import math
def primeFactors(n):
    l= []
    # Print the number of two's that divide n
    while n % 2 == 0:
        if(2 not in l):
            l.append(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):

        # while i divides n , print i ad divide n
        while n % i== 0:
            if(int(i) not in l):
                l.append(int(i))
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        if(int(n) not in l):
            l.append(int(n))
    return(l)

def nthpowerfulnumber(n):
	start = 1
	k= 0
	while(True):
		li = primeFactors(start)
		flagnotpow = False
		for i in li:
			if(start%i!=0 and start%(i*i)!=0):
				flagnotpow = True
				break
		if(flagnotpow == False):
			if(k == n):
				return start
			else:
				k = k+1
		start = start + 1


