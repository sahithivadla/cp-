# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g.
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	indrotated = str2.index(str1[0])
	res = ""
	res = str1[indrotated:]+str1[0:indrotated]
	if(res==str2):
		return True
	else:
		return False
	pass