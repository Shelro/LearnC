class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            isNegative = True
        else:
            isNegative = False
        x = abs(x)
        l = list(str(x))
        if x >= 2**31-1:
            return 0
        else:
            res = 0
            while l:
                res = res*10 + int(l.pop())
        if isNegative:
            res *= (-1)
        return res