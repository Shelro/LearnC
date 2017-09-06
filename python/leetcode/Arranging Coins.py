class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        My Answer: Time limit excceed

        if n<=0:
            return 0
        m = int(math.sqrt(n))
        while m<n:
            temp = m*(m+1)/2
            if temp > n:
                m-=1
            elif temp < n:
                if temp+m+1 > n:
                    return m
                else:
                    m+=1
            else:
                return m
        """

        from math import sqrt
        return int((sqrt(1+8*n) - 1) / 2)