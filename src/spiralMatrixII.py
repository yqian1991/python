class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
		if n==0:
			return [[]]
		rowBegin = 0
		rowEnd = n - 1
		colBegin = 0
		colEnd = n - 1
		res =[[0 for i in range(0, n)] for j in range(0 ,n)]
		number=1
		while rowBegin <= rowEnd and colBegin<=colEnd:
			for i in range(colBegin, colEnd+1):
				res[rowBegin][i] = number
				number += 1
			rowBegin += 1

			for j in range(rowBegin, rowEnd+1):
				res[j][colEnd]=number
				number += 1
			colEnd -= 1

			if rowBegin <= rowEnd:
				for i in range(colEnd, colBegin-1, -1):
					res[rowEnd][i] = number
					number += 1
			rowEnd -= 1

			if colBegin <= colEnd:
				for i in range(rowEnd, rowBegin-1, -1):
					res[i][colBegin] = number
					number += 1
			colBegin += 1
		return res
					
			
if __name__ == "__main__":
	sol = Solution()
	print sol.generateMatrix(3)
