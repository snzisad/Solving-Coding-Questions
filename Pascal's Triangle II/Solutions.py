class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex  += 1
        rows, temp = [], []

        for i in range(rowIndex):
            rows.append(1)
            temp = list(rows)
            for j in range(1,i):
                rows[j] = temp[j]+temp[j-1]

        return rows