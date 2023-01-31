# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None

        # Find the middle element of the array and make it the root of the tree
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        # Create left and right subtrees by recursively calling the same function on the left and right subarrays
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root