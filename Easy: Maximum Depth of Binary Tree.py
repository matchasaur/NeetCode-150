# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        depth = 0
        if (root == None):
            return depth
        depth = max(self.maxDepth(root.right), self.maxDepth(root.left))

        return depth + 1
