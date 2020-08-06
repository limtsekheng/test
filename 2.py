# # print(sum(range(1,3),4))
# # from unicodedata import lookup

# # print(lookup('SOCCER BALL'))

# balance = 200
# def withdraw(x):
# 	nonlocal balance
# 	balance = balance - x
# 	print(balance)
# 	return balance

# withdraw(10)
# import bisect

# a = [2,3,6,8,9,9,8,19,9,12,15,16,18]

# # print(bisect.bisect(a,9))
# def helper(x):
# 	while x <10:
# 		yield x
# 		x += 1

# a = helper(2)
# print(next(a))
# print(next(a))

# class Test:
# 	def __init__(self, num, prop):
# 		self.num = num
# 		self.prop = prop

# a = Test(50,'hehe')
# b = Test(100, 'hoho')
# c = Test(50,'hehe')
# d = a

# print(d)
# print(a)

str = "print('hahaha')"
eval(str)
exec(str)
