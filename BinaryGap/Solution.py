class Solution(object):
    def binaryGap(self, N):
        """
        :type n: int
        :rtype: int
        """

        bin_num = "{0:b}".format(N)
        max_gap, counter, num_1 = 0, 0, 0

        for b in bin_num:
            if b == "1":
                max_gap = max(max_gap, counter)
                counter = 0
                num_1 += 1
            else:
                counter += 1
                
        if num_1>1:
            max_gap += 1
            
        return max_gap