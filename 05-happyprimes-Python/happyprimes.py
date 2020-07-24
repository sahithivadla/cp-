# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After
# some thought, we see that no matter what number we start with, when we keep replacing
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n).
# And that's top-down design! Here we go....
# Note: the autograder will grade each of the following functions, so they are required.
# However, they also are here specifically because they are just the right helper
# functions to make nthHappyNumber(n) easier to write!

def isprime(num):
    c= 0
    for i in range(1,num+1):
        if(num%i == 0):
            c= c+1
    if(c==2):
        return True
    return False

def ishappyprimenumber(n):
    # Your code goes here
    if n==1 or n ==7 :
        return True
    temp = n
    sum= n
    while(sum>9):
        sum =0
        while(temp>0):
            rem = temp%10
            sum=sum+(rem*rem)
            temp = temp //10
        if(sum ==1):
            return True
        temp = sum
    if(sum == 7):
        return True
    return False




