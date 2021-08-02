def func1():
	def func2():
		nonlocal y
		y = 2
	func2()
	print(y)
	
func1()