# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root: return True
        parents = [root]
        while parents:
            children = [child for node in parents if node for child in (node.left, node.right)]
            test = [c.val if c else None for c in children]
            if test != test[::-1]: return False
            parents = children
        return True