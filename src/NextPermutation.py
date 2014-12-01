class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
		n = len(num) - 2
		while n>=0:
			if num[n]<num[n+1]:
				break
			else:
				n -= 1
		if n == -1:
			return reverse(num)
		

		
		
		print num[n]
			
			



if __name__=="__main__":
	sol = Solution()
	sol.nextPermutation([1,4,3,2,1])
