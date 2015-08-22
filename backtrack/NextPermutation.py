class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
		n = len(num) - 2
		while n >= 0:
			if num[n]<num[n+1]:
				break
			else:
				n -= 1
		if n == -1:
			return reverse(num)
		else:
			print n
			small = min(num[(n+1):])
			print small
			small_index = num.index(small)
			num[n], num[small_index] = num[small_index], num[n]
			sorted(num[n+1:])
			return num
			
			
if __name__=="__main__":
	sol = Solution()
	print sol.nextPermutation([1,4,3,2,1])
