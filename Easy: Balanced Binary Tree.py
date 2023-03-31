# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        balance = [True]
        if not root:
            return True
        
        leftDepth = self.DFS(root.left, balance)
        rightDepth = self.DFS(root.right, balance)
        if abs(leftDepth - rightDepth) > 1: balance[0] = False
        return balance[0]

    def DFS(self, root, balance):
        if not root:
            return 0
        
        leftDepth = self.DFS(root.left, balance)
        rightDepth = self.DFS(root.right, balance)
        print(root.val, leftDepth, rightDepth)

        if abs(leftDepth - rightDepth) > 1: balance[0] = False
        return max(leftDepth, rightDepth)+1
