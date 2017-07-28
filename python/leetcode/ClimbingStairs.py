class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        mostT = n / 2
        startO = 0
        if n%2==1:
            startO = 1
        if mostT==0:
            result += 1
        else:
            for i in range(mostT+1):
                index = 2*i + startO
                upcase = 1
                downcase = 1
                for j in range(index):
                    upcase *= (mostT-i+index-j)
                for t in range(1,index+1):
                    downcase *= t
                result += upcase/downcase
        return result