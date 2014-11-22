class Heap:
	def getLargestN(self, s, n):
		res = [0]*n
		for j in range(0, n):
			self.heapify(s)
			res[j]=s[0]
			s = s[1:]
		
		return res
	
	def heapify(self, s):
		i = (len(s)//2) -1
		for k in range(i, -1, -1):
			child = 2*k+1
			#print child

			if child+1<len(s) and s[child+1] > s[child]:
				child = child + 1
			#print child
			if s[k] < s[child]:
				s[k], s[child] = s[child], s[k]
			#print s, k
		#return s	

if __name__ == "__main__":
	h = Heap()
	print h.getLargestN([10, 56, 3, 1, 2, 4, 5, 110, 6, 7, 100], 3)


	