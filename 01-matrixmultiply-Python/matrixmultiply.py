# Write the function matrixMultiply(m1, m2) that takes two 2d lists
# (that we will consider to be matrices) and returns a new 2d list that
# is the result of multiplying the two matrices. Return None if the
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    rows1 = len(m1)
    cols1 = len(m1[0])
    rows2 = len(m2)
    cols2 = len(m2[0])
    # all the rows should contain same number of elements
    for i in range(len(m1)):
        if(cols1 != len(m1[i])):
            return None
    for i in range(len(m2)):
        if(cols2 != len(m2[i])):
            return None

    if(cols1 !=rows2):
        return None
    else:
        # build res
        res =[]
        for i in range(rows1):
            temp =[]
            for j in range(cols2):
                temp.append(0)
            res.append(temp)

        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    res[i][j] = res[i][j]+(m1[i][k]*m2[k][j])

        ans =[]
        for r in res:
            ans.append(r)
        return ans







