# Note: please do not start this problem prior to completing previous problem.
# Bearing in mind the definition of Kaprekar Number from above problem, write the function
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45,
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number,
# nearestKaprekarNumber(50) returns 45.
# Note: as you probably guessed, this also cannot be solved by counting up from 0,
# as that will not be efficient enough to get past the autograder.
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math

def iskaprekar(num):
    ans =num**2
    s= str(ans)
    flag = False
    res= ""
    for i in range(0,len(s)):
        res= res+s[i]
        if(i == len(s)-2):
            res1 = int(s[i+1])
        elif(i == len(s)-1):
            res1 = 0
        else:
            res1 = int(s[i+1:])
        if(int(res) + res1 == num):
            return True
    return False


def fun_nearestkaprekarnumber(n):
    if(len(str(n)) == 2):
        start = n-10
        end = n+10
    elif(len(str(n))==3):
        start = n -100
        end = n+100
    else:
        start = n -1500
        end = n + 1500
    l = []

    for i in range(start, end+1):
        a = math.log10(float(i))- math.floor(math.log10(float(i)))
        if(a!= 0 and iskaprekar(i) == True):
            l.append(i)
    s = []
    for i in l:
        s.append(abs(i-n))
    a = s.index(min(s))
    return(l[a])







