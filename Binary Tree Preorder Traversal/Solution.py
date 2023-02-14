class Solution:
    def preorderTraversal(self, root: TreeNode) -> 'List[int]':
            data = []
            self.helper(root, data)
            return data

    def helper(self, node, data):
        if node:
            data.append(node.val)
            self.helper(node.left, data)
            self.helper(node.right, data)

    def preorderTraversalRecursive(self, root: TreeNode) -> 'List[int]':
        res,stack = [],[root]
        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
        return res