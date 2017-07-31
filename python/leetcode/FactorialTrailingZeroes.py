class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        My answer: Time Limit Error
        result = 1
        if n==0:
            return 0
        for i in range(1,n+1):
            result *= i
        sresult = list(str(result))
        for j in range(1, len(sresult)+1):
            if sresult[len(sresult) - j] != '0':
                return j-1
        """
        return 0 if n < 5 else n/5 + self.trailingZeroes(n/5)