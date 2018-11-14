
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printNode(self):
    	print self.val
    	if self.next != None:
    		self.next.printNode()


class Solution:
    def removeDups(self, head):

    	valset = set([head.val])
    	node = head
    	while node.next != None:
    		if node.next.val in valset:
    			node.next = node.next.next
    		else:
    			valset.add(node.next.val)
    			node = node.next

    	return head


    def isPalindrome(self, head):

    	revnode = None

    	# reverse linked list
    	node = head
    	while node.next != None:
    		revhead = ListNode(node.val)
    		revhead.next = revnode
    		revnode = revhead
    		node = node.next

    	revhead = ListNode(node.val)
    	revhead.next = revnode


    	# iterate through and compare to reversed
    	node = head
    	revnode = revhead
    	while node.next != None :

    		if(node.val != revnode.val):
    			return False

    		node = node.next
    		revnode = revnode.next


    	return True











# Main Function
if __name__ == '__main__':        
    
    case0 = ListNode(1)
    case0.next = ListNode(2)
    case0.next.next = ListNode(3)
    case0.next.next.next = ListNode(1)
    case0.next.next.next.next = ListNode(1)
    #case0.printNode()

    soln = Solution()
    case0s = soln.removeDups(case0)
    print "final result: "
    case0s.printNode()


    case0 = ListNode(1)
    case0.next = ListNode(2)
    case0.next.next = ListNode(3)
    case0.next.next.next = ListNode(2)
    case0.next.next.next.next = ListNode(2)

    print soln.isPalindrome(case0)


