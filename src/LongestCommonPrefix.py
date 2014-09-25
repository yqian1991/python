'''
Created on Sep 23, 2014

@author: yqian33
'''
class Solution:
    # @return a string
    def makeTrie(self, strs):
        root = {}
        for str in strs:
            trie = root
            for ch in str:
                trie = trie.setdefault(ch, {})#set the ch key if not exist and return the value corrspond to key
                print ch, root
            trie = trie.setdefault("", "")
            print trie
        
        return root
            
    def longestCommonPrefix(self, strs):
        root = self.makeTrie(strs)
        print root
        l = len(root)
        result=""
        while len(root) is 1:
            k = root.keys()[0]
            result += str(k)
            root = root[k]
        return result
             
if __name__ == '__main__':
    strs=["ababc"]
    sol = Solution()
    print sol.longestCommonPrefix(strs)
    pass