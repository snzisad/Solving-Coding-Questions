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
        if root is None:
            return 0
        
        def max_height(root):
            left = 0
            right = 0

            if root.left:
                left = 1+max_height(root.left)
            if root.right:
                right = 1+max_height(root.right)
            if root.left is None and root.right is None:
                return 0
        
            return max(left, right)
        
        return max_height(root)+1