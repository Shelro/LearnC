class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        elif n==1:
            return True
        while n>1:
            if n%3!=0:
                return False
            n /= 3
        return True
        """
        Faster Solution:

        MAX_INT = 1162261467
        if n <= 0 or n > MAX_INT:
            return False
        return MAX_INT % n == 0
        """