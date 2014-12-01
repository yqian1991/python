'''
Created on Nov 7, 2014

@author: yqian33
'''
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        add = 0
        al = len(a)-1
        bl = len(b)-1
        res=[]
        while al>=0 and bl>=0:
            temp = int(a[al]) + int(b[bl]) + add
            res.insert(0, str(temp%2))
            print temp, str(temp%2), add
            if temp>=2:
                add = 1
            else:
                add = 0
            al -= 1
            bl -= 1

        while al>=0:
            temp = int(a[al]) + add
            res.insert(0, str(temp%2))
            if temp>=2:
                add = 1
            else:
                add = 0
            al -= 1
            
        while bl>=0:
            temp = int(b[bl]) + add
            res.insert(0, str(temp%2))
            if temp>=2:
                add = 1
            else:
                add = 0
            bl -= 1
            
        if add>0:
            res.insert(0, "1")
        
        #print res 
        str1=''.join(res)  
        return str1
            
            
        
if __name__ == '__main__':
    sol = Solution()
    print sol.addBinary("101111", "10")
    pass