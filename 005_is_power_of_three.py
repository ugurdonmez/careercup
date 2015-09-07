'''

int is_power_of_3(uint32_t n)
return 1 if yes, 0 otherwise. 

'''

import math

def is_power_of_three(n):
	if n == 0:
		return False
	else:
		r = math.log(n) / math.log(3)
		if (r - int(r)) == 0:
			return True
		else:
			return False


print is_power_of_three(27)
print is_power_of_three(0)
print is_power_of_three(3)
print is_power_of_three(42)