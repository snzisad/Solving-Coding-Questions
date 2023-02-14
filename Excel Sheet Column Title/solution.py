class Solution:
    def convertToTitle(self, n: int) -> str:
        ref = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s = ""
        while n > 0:
            n = n-1
            s = ref[n % 26] + s
            n = n // 26

        return s