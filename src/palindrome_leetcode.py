class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s=='':
            return True
        else:
            i=0
            size = len(s)-1
            #print size
            while i < size :
                if not s[i].isalpha():
                    i+=1
                elif not s[size].isalpha():
                    size-=1
                elif s[i].upper()==s[size].upper():
                    i+=1
                    size-=1
                else:
                    return False
            if (i==size and s[i] == s[size]) or i-size==1 :
                return True
     # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        totalLayer = len(triangle)
        print totalLayer
        layer = 1  #num = layer + 1
        while layer<=totalLayer-1:
            for index in range(0, layer+1):
                a = index
                #layer*(layer-1)/2+index and layer*(layer-1)/2+index-1 check index<0 and index>layer
                if index-1<0:
                    a1=999999
                else:
                    a1 = triangle[layer-1][index-1]

                if index>layer-1:
                    b1=999999
                else:
                    b1 = triangle[layer-1][index]

                if a1>b1:
                    triangle[layer][a] += b1
                else:
                    triangle[layer][a] += a1
                #str[a] = str (a1<b1?a1:b1)
                
            layer += 1 
        print triangle[totalLayer-1] 
        return min(triangle[totalLayer-1])

if __name__=='__main__':

    sol = Solution()
    #res = sol.isPalindrome('A man, a plan, a canal: Panama')
    res = sol.isPalindrome('aa')
    #res2 = sol.minimumTotal([[2], [3,4],[6,5,7],[4,1,8,3]])
    res2 = sol.minimumTotal([[-7],[-2,1],[-5,-5,9],[-4,-5,4,4],[-6,-6,2,-1,-5],[3,7,8,-3,7,-9],[-9,-1,-9,6,9,0,7],[-7,0,-6,-8,7,1,-4,9],[-3,2,-6,-9,-7,-6,-9,4,0],[-8,-6,-3,-9,-2,-6,7,-5,0,7],[-9,-1,-2,4,-2,4,4,-1,2,-5,5],[1,1,-6,1,-2,-4,4,-2,6,-6,0,6],[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]])
    print res2
