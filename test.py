class StackList():
	def __init__(self):
		self.items = []

	def getTop(self):
		if not self.isEmpty():
			return self.items[-1]

		else:
			return None

	def push(self, newItem):
		self.items.append(newItem)

	def pop(self):
		if not self.isEmpty():
			self.items.pop()
			return True
		else:
			return False

	def isEmpty(self):
		return len(self.items) == 0



def matchBracket(input):
	openBrackets = ['(','[','{']
	closeBrackets = [')',']','}']
	bracketStack = StackList()

	for cur in input:
		if cur in openBrackets:
			idx = openBrackets.index(cur)
			bracketStack.push(closeBrackets[idx])

		elif cur in closeBrackets:
			if bracketStack.isEmpty() or \
				bracketStack.getTop()!= cur:
				return False
			else:
				bracketStack.pop()

	return bracketStack.isEmpty()

data = ('{','{','[','{','}',']','}','}')
print(matchBracket(data))


### this is to test git ###