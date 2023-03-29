# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None):
            return head
        if (head.next == None):
            return head

        myStack = deque()
        currNode = head
        while (currNode != None):
            myStack.append(currNode)
            currNode = currNode.next

        currNode = myStack.pop()
        head = currNode
        while (len(myStack) != 0):
            tempNode = myStack.pop()
            currNode.next = tempNode
            currNode = tempNode
        currNode.next = None
        return head
