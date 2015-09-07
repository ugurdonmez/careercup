def one_edit_way(str1, str2):
	len1 = len(str1)
	len2 = len(str2)

	if abs(len1 - len2) > 1:
		return False
	elif len1 == len2:
		diff = 0
		for i in range(0,len1):
			if str1[i] != str2[i]:
				diff = diff + 1
				if diff == 2:
					return False
		return True
	else:
		if len1 > len2 :
			i = 0
			j = 0
			while i < len1:
				if str1[i] == str2[j]:
					i = i + 1
					j = j + 1
					if j == len2:
						return True
				else:
					i = i + 1
					if i > j + 1:
						return False
			return True
		else:
			return one_edit_way(str2, str1)




a = "abc"
b = "ab"
c = "adc"
d = "cab"

print one_edit_way(a,b)
print one_edit_way(a,c)
print one_edit_way(a,d)