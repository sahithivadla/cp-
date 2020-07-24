# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0
# and which remains prime when the leading (left) digit is successively removed.
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime.
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and
# nthLeftTruncatablePrime(10) returns 53.



import math

def isprime(num):
    c =0
    for i in range(1,num+1):
        if(num%i == 0):
            c= c+1
    if(c==2):
        return True
    return False

def fun_nth_lefttruncatableprime(n):
    l =[2,3,5,7,13,17]
    k =0
    start = 2
    while(True):
        flagnotprime = False
        if((len(str(start)) ==1 or len(str(start)) ==2) and  start in l):
                if(k ==n):
                    return start
                else:
                    k = k+1
        else:
            if(isprime(start) == True):
                s=str(start)
                for i in range(1,len(s)):
                    if(isprime(int(s[i:])) == False):
                        flagnotprime = True
                        break
                if(flagnotprime == False):
                    if(k==n):
                        return start
                    else:
                        k = k+1
        start = start + 1








