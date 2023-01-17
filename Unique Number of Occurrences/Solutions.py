class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        occurances = {}

        for c in arr:
            if c in occurances:
                occurances[c] += 1
            else:
                occurances[c] = 1

        unique_set = set()
        for val in occurances.values():
            if val in unique_set:
                return False
            unique_set.add(val)

        return True