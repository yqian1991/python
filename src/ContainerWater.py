'''
Created on Nov 21, 2014

@author: yqian33
'''
class Solution:
    # @return an integer
    def maxArea(self, A):
        start = 0
        end = len(A)-1
        
        maxc = -100
        while start < end:
            contain = min(A[start], A[end])*(end-start)
            maxc = max(maxc, contain)
            if A[start] < A[end]:
                start += 1
            else:
                end -= 1
        return maxc
          
if __name__ == '__main__':
    sol = Solution()
    print sol.maxArea([0,1,0,2,1,0,1,3,2,1,2,1])
    pass