class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        a = len(s1)
        b = len(s2)
        c = len(s3)
        #print a, b, c
        
        if a+b is not c:
            return False
        
        elif a == 0:
            if s2 == s3:
                return True
            else:
                return False
        elif b == 0:
            if s1 == s3:
                return True
            else:
                return False
        else:
            i=0
            j=0
            
            mylist = [ [0 for i in range(0, b+1)] for i in range(0, a+1)]
            mylist[0][0] = 1
            for i in range(1, a+1):
                if s1[i-1] is s3[i-1]:
                    mylist[i][0] = 1
                    #print mylist[i][0]
                else:
                    break
            for i in range(1, b+1):
                if s2[i-1] is s3[i-1]:
                    mylist[0][i] = 1
                    #print mylist[0][i]
                else:
                    break
            #print mylist
            for i in range(1, b+1):
                for j in range(1, a+1):
                    if s3[i+j-1] is s1[i-1]:
                        #print 'a'
                        mylist[i][j] = mylist[i-1][j] or mylist[i][j]
                    if s3[i+j-1] is s2[j-1]:
                        #print 'd'
                        mylist[i][j] = mylist[i][j-1] or mylist[i][j]
        
        print mylist
        if mylist[a][b] == 1:
            return True
        else:
            return False

if __name__ == "__main__":
    s1 = "aabc"
    s2 = "abad"
    s3 = "aabadabc"
    sol = Solution()
    print sol.isInterleave(s1, s2, s3)
                        
                        
                
