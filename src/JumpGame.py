class Solution:
    # @param A, a list of integers
    # @return a boolean
	step=0
	def helper(self, A, idx):
		if idx == len(A)-1:
			return True
		
		for i in range(1, A[idx]+1):
			self.step += 1
			if self.helper(A, idx+i):
				return True
			self.step -= 1
		return False	
		
	def canJump1(self, A):
		if len(A)==0:
			return 0
		else:
			idx = 0
			self.helper(A, idx)
			return self.step

	def canJump(self, A):
		maxCover = 0
		i = 0
		while i <= maxCover and i<len(A):
			print i, maxCover
			if A[i]+i>maxCover:
				maxCover = A[i] + i
			if maxCover>=len(A)-1:
				return True
			i += 1
		return False
			
if __name__=='__main__':
	sol = Solution()
	s=[2,3,1,1,4]
	print sol.canJump1(s)
	#print sol.canJump1(s)