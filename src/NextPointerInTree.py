# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing

    def connect(self, root):
		if root == None:
			return 
		if root.left == None and root.right == None:
			return
		
		last = root.right 
		if last == None:
			last = root.left

		first = root.next

		while True:
		    if first == None:
		    	break
		    #as far as somne of our right brothers has children we shoudl link our last with it.
		    if first.left != None:
		        last.next = first.left
		        break
		    if first.right != None:
		        last.next = first.right
		        break

		    first = first.next

		if root.left != None and root.right != None:
		        root.left.next = root.right

		connect(root.right)
		connect(root.left)