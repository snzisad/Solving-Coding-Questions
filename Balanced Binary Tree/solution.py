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
        if root is None:
			return True
        return abs(self.helper(root.left)-self.helper(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def helper(self,node):
        if not node:
            return 0
        return max(self.helper(node.left),self.helper(node.right))+1

