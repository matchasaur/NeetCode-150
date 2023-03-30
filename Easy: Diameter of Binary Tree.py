# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
global currMax
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global currMax
        currMax = 0
        leftMax = self.leftPath(root.left)
        rightMax = self.rightPath(root.right)
        return max(leftMax + rightMax, currMax)

    def leftPath(self, root):
        if (root is None):
            return 0
        global currMax
        leftMax = self.leftPath(root.left)
        rightMax = self.leftPath(root.right)
        currMax = max(currMax, leftMax + rightMax)
        return max(leftMax, rightMax)+1


    def rightPath(self,root):
        if (root is None):
            return 0
        global currMax
        leftMax = self.rightPath(root.left)
        rightMax = self.rightPath(root.right)
        currMax = max(currMax, leftMax + rightMax)
        return max(leftMax, rightMax)+1
