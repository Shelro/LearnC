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
        res = 0
        while l:
            res = res*10 + int(l.pop())
        if res > 2**31:
            return 0
        if isNegative:
            res *= (-1)
        return res
