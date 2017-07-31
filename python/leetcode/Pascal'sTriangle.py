class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        temp = []
        for i in range(numRows):
            res = []
            res.append(1)
            if i>0:
                for t in range(len(temp[i-1])-1):
                    res.append(temp[i-1][t]+temp[i-1][t+1])
                res.append(1)
            temp.append(res)
        return temp