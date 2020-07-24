# Background: a Kaprekar number is a non-negative integer, the representation of whose square
# can be split into two possibly-different-length parts (where the right part is not zero)
# that add up to the original number again. For instance, 45 is a Kaprekar number, because
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,...
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n
# and returns the nth Kaprekar number, where as usual we start counting at n==0.

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


def fun_nth_kaprekarnumber(n):
    start = 1
    k = 0
    while(True):
        if(start%10 == 0):
            continue
        else:
            if(iskaprekar(start) == True):
                if(k == n):
                    return start
                else :
                    k = k + 1
        start = start +1












