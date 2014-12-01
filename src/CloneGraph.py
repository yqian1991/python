'''
Created on Nov 24, 2014

@author: yqian33
'''
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        head = UndirectedGraphNode(node.label)
        l = []
        l.append(node)
        dict1 = {}
        dict1[node] = head
        while len(l) != 0:
            cur = l.pop()
            if len(cur.neighbors) != 0:
                for n in cur.neighbors:
                    if n not in dict1:
                        nnode = UndirectedGraphNode(n.label)
                        dict1[n] = nnode
                        dict1[cur].neighbors.append(nnode)
                        l.append(n)
                    else:
                        dict1[cur].neighbors.append(dict1[n])
        return head
            
        
if __name__ == '__main__':
    node = UndirectedGraphNode(0)
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)
    
    node.neighbors=[node1, node2]
    
    sol = Solution()
    sol.cloneGraph(node)
    pass