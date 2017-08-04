class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for p in 2, 3, 5:
            while num % p == 0 < num: //a == b < c actually means a == b and b < c
                num /= p
        return num == 1