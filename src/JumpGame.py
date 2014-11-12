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
	#s=[2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
	print sol.canJump1(s)
	#print sol.canJump1(s)