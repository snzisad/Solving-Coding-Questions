class Solution(object):
    def rotate(self, A, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        len_A = len(A)
        K = K % len_A

        if K == 0:
            return A

        temp = list(A)

        i = len_A-1
        while (i-K) >= 0:
            A[i] = temp[i-K]
            i -= 1

        i = len_A-1
        K -= 1
        while K>=0:
            A[K] = temp[i]
            i -= 1
            K -= 1

        return A