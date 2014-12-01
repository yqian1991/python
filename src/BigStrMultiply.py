'''
Created on Oct 1, 2014

@author: yqian33
'''
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        l1 = len(num1)
        l2 = len(num2)
        result=""
        res=[0 for i in range(0, l1+l2-1)]

        j = l2 -1
        while j>=0:
            i = l1 -1
            while i>=0:
                res[i+j] += int(num1[i]) * int(num2[j])
                i -= 1
            j -= 1
        print res    
        
        temp=0
        i = len(res)-1
        while i >= 0:
            tmpres = res[i]
            res[i] = (res[i] + temp ) % 10 
            temp = (tmpres + temp ) / 10
            i -= 1
        if temp:
            res.insert(0, temp)
        print res
           
        for i in range(0, len(res)) :
            result += str(res[i])
        return result
        
if __name__ == '__main__':
    sol = Solution()
    print sol.multiply("999003245682345782683534562354235423405000", "887634539004252345234652354600099")
    pass