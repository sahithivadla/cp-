# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number.
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8,
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.
def div( a, b ):
    while a % b == 0:
        a = a / b
    return a

def isUgly( no ):
    no = div(no, 2)
    no = div(no, 3)
    no = div(no, 5)
    return 1 if no == 1 else 0

def fun_nth_uglynumber(n):
    start = 1
    k = 0
    while(True):
        if(isUgly(start)):
            if(k == n):
                return start
            else:
                k= k+1
        start = start + 1
