class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def backtrack(self, index, num, n, res):
        if index == n:
            res.append(num[:])
        else:
            flag = 0
            for i in range(index, n+1):
                for j in range(index, i):
                    if num[j] == num[i]:
                        flag = 1
                        break
                    flag = 0
                if flag == 1:
                    continue
                num[i], num[index] = num[index], num[i]
                self.backtrack(index+1, num, n, res)
                num[i], num[index] = num[index], num[i]
                
    def permuteUnique(self, num):
        num = sorted(num)
        res=[]
        self.backtrack(0, num, len(num)-1, res)
        return res

if __name__== "__main__":
    sol = Solution()
    print sol.permuteUnique([1,1,2,2,3 ,4])