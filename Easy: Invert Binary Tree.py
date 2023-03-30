# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.invertHelp(root)

    def invertHelp(self, node):
        if (node == None):
            return None

        leftChild = self.invertHelp(node.left)
        rightChild = self.invertHelp(node.right)

        node.left = rightChild
        node.right = leftChild

        return node
