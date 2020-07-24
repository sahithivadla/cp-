# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number.
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def fun_nth_tidynumber(n):
    start = 1
    k = 0
    s=[]
    while(True):
        s = list(map(int,str(start)))
        s.sort()
        if(start == int(''.join(map(int,s)))):
            if(k == n):
                return start
            else:
                k = k +1
        start = start + 1
