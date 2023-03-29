# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        currNode = head.next

        while currNode and head and currNode.next:
            if(currNode == head):
                return True
            currNode = currNode.next.next
            head = head.next
        return False
