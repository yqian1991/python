class Solution:
    # @param A, a list of integers
    # @return a boolean
	def jump(self, A):
		ret = 0
		last1 = 0
		curr =0
		for i in range(0, len(A)):
			if i>last1:
				last1 = curr
				ret += 1
			curr = max(curr, i+A[i])
		return ret
        

if __name__=='__main__':
	sol = Solution()
	s=[2, 3, 1, 1, 4]
	print sol.jump(s)
	#print sol.canJump1(s)