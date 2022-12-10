# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        def travarse(root):
            if root:
                travarse(root.left)
                self.result.append(root.val)
                travarse(root.right)
        
        self.result = []
        travarse(root)
        
        return self.result


        