class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        item_count = {}
        max_val = 0
        max_val_count = 0

        for item in nums:
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1

            
            if max_val_count < item_count[item]:
                max_val_count = item_count[item]
                max_val = item

        return max_val

