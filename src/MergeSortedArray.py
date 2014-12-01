class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
	def merge(self, A, m, B, n):
		abIndex = m+n-1
		aIndex = m-1
		bIndex = n-1

		while aIndex>=0 and bIndex>=0:
			if A[aIndex]>B[bIndex]:
				A[abIndex] = A[aIndex]
				aIndex -= 1
				abIndex -= 1
			elif A[aIndex]<=B[bIndex]:
				A[abIndex] = B[bIndex]
				bIndex -= 1
				abIndex -= 1
		#print A, bIndex, abIndex
		while bIndex>=0:
			A[abIndex] = B[bIndex]
			abIndex -= 1
			bIndex -= 1
			#print A
		return
		
				
			
if __name__ == "__main__":
	sol = Solution()
	A =[4, 5, 6, 0, 0, 0]
	sol.merge(A, 3, [1, 2, 3], 3)
	print A
