class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        temp = []
        for i in range(rowIndex):
            res = [1]
            for t in range(len(temp)-1):
                res.append(temp[t]+temp[t+1])
            res.append(1)
            temp = res
        return res
"""
Better Solution:(Much quicker)
        
        row = [1]
        r0 = 1
        for k in range(1, rowIndex+1):
            r0 = r0 * (rowIndex-k+1) /k
            row.append(r0)
        return row
"""