def isDigit(char):
	if char >= '0' and char <= '9':
		return True
	else:
		return False

def calculate(char1, char2, op):
	if op == '+':
		return char1 + char2
	elif op == '-':
		return char1 - char2
	elif op == '*':
		return char1 * char2
	elif op == '/':
		return char1 / char2

def postfix_calculator(str):
	stack = []
	for i in range(0, len(str)):
		if isDigit(str[i]):
			stack.append(int(str[i]))
		else:
			stack.append(calculate( stack.pop(), stack.pop(), str[i]))

	return stack.pop()

print postfix_calculator("432+*")