# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(list1 is None and list2 is None):
            return list1
        elif(list1 is None and list2 is not None):
            return list2
        elif(list1 is not None and list2 is None):
            return list1

        if (list1.val < list2.val):
            currNode = list1
            list1 = list1.next
        else:
            currNode = list2
            list2 = list2.next

        head = currNode
       
        while(list1 is not None and list2 is not None):
            if (list1.val < list2.val):
                currNode.next = list1
                currNode = currNode.next
                list1 = list1.next
            else:
                currNode.next = list2
                currNode = currNode.next
                list2 = list2.next

        if(list1 is None):
            currNode.next = list2
        elif(list2 is None):
            currNode.next = list1

        return head
