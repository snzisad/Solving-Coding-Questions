class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pairs = {}

        for c in nums:
            if c in pairs:
                pairs[c] += 1
            else:
                pairs[c] = 1

        for key, value in pairs.items():
            if value %2 != 0:
                return key