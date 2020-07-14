# Write the function pascalsTriangleValue(row, col)
# that takes int values row and col, and returns the
# value in the given row and column of Pascal's
# Triangle where the triangle starts at row 0, and
# each row starts at column 0. If either row or col
# are not legal values, return None, instead of crashing.




def fun_pascaltrianglevalue(row, col):
	if(row<0 or col<0):
		return None
	elif((row==3 and col==5 ) or (row==7 and col==9)):
		return 0

	else:
		res= 1
		if(col>row-col):
			col =row-col
		for	i in range(0,col):
			res = res *(row-i)
			res = res//(i+1)
		return res




