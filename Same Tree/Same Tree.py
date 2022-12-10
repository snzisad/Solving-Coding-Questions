# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))


    def isSameTree2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if p == q:
            return True
        elif not p or not q:
            return False
        
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            root1 = stack1.pop()
            root2 = stack2.pop()
            
            if root1.val != root2.val:
                return False
            
            if root1.left:
                if not root2.left:
                    return False
                stack1.append(root1.left)
                
            if root1.right:
                if not root2.right:
                    return False
                stack1.append(root1.right)
                
            if root2.left:
                if not root1.left:
                    return False
                stack2.append(root2.left)
                
            if root2.right:
                if not root1.right:
                    return False
                stack2.append(root2.right)
            
        
        return len(stack1) == len(stack2) == 0