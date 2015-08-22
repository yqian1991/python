class Solution:
    # @return a boolean
    def isMatch(self, s, p):
		sIndex = 0
		pIndex = 0
		sl = len(s)
		pl = len(p)

		if p[pIndex+1] != '*':
			if sIndex == sl-1:
				return False
			if p[pIndex] != '.' and s[sIndex]!= p[pIndex]:
				return False
			return self.isMatch()
			
			
		
                
if __name__=='__main__':
	sol = Solution()
	print sol.isMatch("abbbcd", "ab*bbbcd")