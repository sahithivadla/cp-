# Write the function nearestBusStop(street) that takes a
# non-negative int street number, and returns the nearest
# bus stop to the given street, where buses stop every 8th street,
# including street 0, and ties go to the lower street,
# so the nearest bus stop to 12th street is 8th street,
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):

	c= street -(street%8)
	c1 =(street+8) - (street%8)
	if(abs(street-c) <= abs(c1-street)):
		return abs(street-c)
	else:
		return abs(c1-street)

