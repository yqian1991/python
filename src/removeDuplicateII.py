# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
		if head is None:
			return None
		nhead = ListNode(0)
		nhead.next = head
		nhead1 = nhead
		cur = head
		while cur is not None and cur.next is not None:
			if cur.next.val == cur.val:
				while cur.next is not None and cur.next.val == cur.val:
					cur = cur.next
				nhead1.next = cur.next
				cur = cur.next
				#nhead1 = cur
			else:
				#if cur.next is not None and cur.next.val != cur.next.next.val:
				#	nhead1 = cur.next
				nhead1 = cur
				cur = cur.next
				
		return nhead.next
	
    def printList(self, h):
		while h is not None:
			print h.val
			h = h.next
			
		
				

if __name__ == "__main__":

	t1 = ListNode(1)
	t2 = ListNode(1)
	t3 = ListNode(2)
	t4 = ListNode(3)
	t5 = ListNode(3)
	t6 = ListNode(4)
	t7 = ListNode(5)
	t8 = ListNode(5)
	t1.next = t2
	t2.next = t3
	t3.next = t4
	t4.next = t5
	t5.next = t6
	t6.next = t7
	t7.next = t8

	sol = Solution()
	sol.printList(sol.deleteDuplicates(t1))