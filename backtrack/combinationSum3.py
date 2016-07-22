class Solution(object):
    def __init__(self):
        self.temp = []
        self.result = []

    def helper(self, k, n, g):
        if n < 0:
            #self.temp = []
            return
        if k == 0 and n == 0:
            print self.temp
            c = self.temp[:]
            if c not in self.result:
                self.result.append(c)
                print self.result

        for i in range(0, k):
            for j in range(g, 10):
                if j not in self.temp:
                    self.temp.append(j)
                    print self.temp, k-1, n-j, j+1
                    if n-j >= 0:
                        self.helper(k-1, n-j, j+1)
                    del_index = self.temp.index(j)
                    del self.temp[del_index]

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        g = 1
        self.helper(k, n, g)
        return self.result

sol = Solution()
#print sol.combinationSum3(3, 7)
#print sol.combinationSum3(3, 9)
print sol.combinationSum3(8, 36)
