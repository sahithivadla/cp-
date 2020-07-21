# Write the function nthSmithNumber that takes a non-negative int n
# and returns the nth Smith number, where a Smith number is a composite (non-prime)
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1).
# Note that if a prime number divides the Smith number multiple times, its digit sum
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def isprime(n):


import math
def primeFactors(n):
   # no of even divisibility
   while n % 2 == 0:
      print (2),
      n = n / 2
   # n reduces to become odd
   for i in range(3,int(math.sqrt(n))+1,2):
      # while i divides n
      while n % i== 0:
         print (i)
         n = n / i
   # if n is a prime
   if n > 2:
      print (n)
def fun_nth_smithnumber(n):
    c=0
    while(True):