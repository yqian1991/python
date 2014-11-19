class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
	def subsets(self, S):
		S = sorted(S)
		n = len(S)
		if n == 0:
			return []
		else:
			tmp=[]
			res=[[]]
			self.helper(S, 0, tmp, res)
			return res
	def helper(self, s, i, tmp, res):
		for i in range(i, len(s)):
			tmp.append(s[i])
			cur = tmp[:]
			res.append(cur)
			print tmp
			self.helper(s, i+1, tmp, res)
			tmp.pop()
			print tmp

if __name__=="__main__":
	sol = Solution()
	print sol.subsets([1,2,2])
			
		
		