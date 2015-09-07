'''

Given a positive integer, rearrange its digits to find the greatest positive integer. 

'''

def find_greatest_positive_integer(str):
	digits = []
	for i in range(0,10):
		digits.append(0)

	for i in range(0, len(str)):
		digits[ int( str[i]) ] = digits[ int(str[i]) ] + 1

	result = 0
	for i in reversed(range(10)):
		for j in range(0, digits[i]):
			result = result * 10 + i

	return result


print find_greatest_positive_integer("123")
print find_greatest_positive_integer("1239900")