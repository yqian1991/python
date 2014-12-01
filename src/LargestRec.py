'''
Created on Oct 17, 2014

@author: yqian33
'''
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        stack=[]
        height.append(0)
        sum = 0
        i = 0
        while i < len(height):
            if len(stack) == 0 or height[i]>height[stack[-1]]:
                stack.append(i)
            else:
                tmp = stack[-1]
                stack.pop()
                cur=0
                if len(stack)==0:
                    cur = i
                else:
                    cur = i-stack[-1]-1
                sum = max(sum, height[tmp]*cur)
                #print 'sum:',sum
                i -= 1
            i += 1
        return sum
        
        
if __name__ == '__main__':
    sol = Solution()
    print sol.largestRectangleArea([2,1,5,6,2,3])
    pass