'''

Give four points, determine is it is a square, rectangle or none of the above.

'''

import math

def calculate_distance(p1, p2):
	return math.sqrt( (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]) )

def square_rectangle(p1, p2, p3, p4):
	distances = []

	distances.append(calculate_distance(p1,p2))
	distances.append(calculate_distance(p1,p3))
	distances.append(calculate_distance(p1,p4))
	distances.append(calculate_distance(p2,p3))
	distances.append(calculate_distance(p2,p4))
	distances.append(calculate_distance(p3,p4))

	distances.sort()

	if distances[0] == distances[1] and distances[1] == distances[2] and distances[2] == distances[3] and distances[3] != distances[4] and distances[4] == distances[5]:
		return "square"
	elif distances[0] == distances[1] and distances[1] != distances[2] and distances[2] == distances[3] and distances[3] != distances[4] and distances[4] == distances[5]:
		return "rectangle"
	else:
		return "nothing"


print square_rectangle( [0,1], [1,0], [1,1], [0,0] )
print square_rectangle( [1,1], [1,0], [1,1], [0,0] )
print square_rectangle( [2,1], [2,0], [0,1], [0,0] )