
class HashTable:
	def __init__(self, length=10):
		self.array = [None] * length
	
	def hash(self, key):
		return hash(key) % len(self.array)
	
	def add(self, key, val):
		index = self.hash(key)
		if self.array[index] is not None:
			for keyVal in self.array[index]:
				if keyVal[0] == key:
					keyVal[1] = val
					break
			else:
				self.array[index].append([key, val])
		else:
			self.array[index] = []
			self.array[index].append([key, val])
		
	def get(self, key):
		index = hash(key)
		if self.array[index] is None:
			raise KeyError()
		else:
			for keyVal in self.array[index]:
				if keyVal[0] == key:
					return keyVal[1]
			raise KeyError()

	def printTable(self):
		if len(self.array) > 0:
			# for element in self.array:
			# 	print(element)
			print(self.array)

h = HashTable()
h.add(1, 'a')
h.add(2, 'b')
h.add(4, 'c')
h.add(4, 'd')
h.printTable()

