class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def help(self, candidates, target, index, res, tmp):
        #print tmp, target
        if target == 0:
            re = tmp[:]
            res.append(re)
            tmp=[]
            return res
        elif (index == len(candidates)) or target<0:
            return res
        else:
            for i in range(index, len(candidates)):
                if i>index and candidates[i] == candidates[i-1]:
					continue;
                
                tmp.append(candidates[i])
                #print tmp
                self.help(candidates, target-candidates[i], i+1, res, tmp)
                tmp.pop()
                
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        if len(candidates) == 0:
            return []
        else:
            res=[]
            tmp=[]
            self.help(candidates, target, 0, res, tmp)
            return res

if __name__=="__main__":
	sol = Solution()
	s=[13,23,25,11,7,26,14,11,27,27,26,12,8,20,22,34,27,17,5,26,31,11,16,27,13,20,29,18,7,14,13,15,25,25,21,27,16,22,33,8,15,25,16,18,10,25,9,24,7,32,15,26,30,19]
	print sol.combinationSum2(s, 25)
