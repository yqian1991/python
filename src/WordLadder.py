class Solution:

# @param start, a string
# @param end, a string
# @param dict, a set of string
# @return a list of lists of string
    def findLadders(self, start, end, dict):
        path = []
        if start == end:
            path.append(end)
            res.append(path)
            return res
        dict.add(start)
        #print dict
        dict.add(end)
        #print dict

        #construct word graph
        edge = {}
        for word in dict:
            edge[word] = []
        for word in dict:
            #print word
            for i in range(len(word)):
                #print range(ord(word[i])+1, 123)
                for c in range(ord(word[i])+1, 123):
                    nw = word[:i] + chr(c) + word[i+1:]
                    #print nw
                    if nw in dict:
                        #print nw
                        edge[word].append(nw)
                        edge[nw].append(word)

        #search the graph
        res = []
        queue = [[start]]
        flag = 0
        delete = set([start])
        size = 1
        add = []
        while len(queue):
            words = queue.pop(0)
            if flag and len(words) >= flag:
                break
            if len(words) > size:
                size = len(words)
                delete |= set(add)
                add = []
            word = words[-1]
            #print word
            for nw in edge[word]:
                if nw == end:
                    flag = len(words) + 1
                    res.append(words + [nw])
                if nw not in delete:
                    queue.append(words + [nw])
                    add.append(nw)
        return res

    
if __name__=='__main__':
    start = 'hit'
    end = 'cog'
    dict = set(['hot','dot','dog','lot','log'])

    sol = Solution()
    res = sol.findLadders(start, end, dict)
    print res
