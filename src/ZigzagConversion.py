'''
Created on Sep 22, 2014

@author: yqian33
'''
class Solution:
    # @return a string
    def convert(self, s, nRows):
        print s
        l = len(s)
        #print l
        if l <= nRows or nRows == 1:
            return s
        steps = 2*nRows - 2
        
        result=""
        #index, s[0], s[0+steps], s[0+steps+steps]
        for i in range(0, nRows):
            j = 0
            while (i + steps*j)<l:
                temp1 = s[i + steps*j]
                #print temp1
                if i>0 and i<nRows-1 and steps*j + nRows - 1 + nRows - 1 - i <l:
                    temp2 = s[ steps*j + nRows - 1 + nRows - 1 - i] 
                    #print temp2
                    result += temp1+temp2
                else:
                    result += temp1
                j += 1
      
        return result               
    
if __name__ == '__main__':
    sol = Solution()
    print sol.convert("PAYPALISHIRING", 3)
    pass