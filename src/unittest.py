class Test:
	"""
	>>> a = Test(s)
	>>>a.multiply_by_2()
	10
	"""
	def __init__(self, number):
		self._number = number
	
	def multiply_by_2(self):
		return self._number*2