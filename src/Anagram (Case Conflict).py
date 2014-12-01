'''
Created on Nov 3, 2014

@author: yqian33
'''
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        import collections
        count = collections.Counter([tuple(sorted(s)) for s in strs])
        print count
        return filter(lambda x: count[tuple(sorted(x))]>1, strs)
if __name__ == '__main__':
    sol = Solution()
    print sol.anagrams(["qianyu", "yuqian", "yurtq"])
    print tuple(sorted("sgfa"))
    pass