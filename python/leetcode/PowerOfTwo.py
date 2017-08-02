class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        while n>1:
            if n%2!=0:
                return False
            else:
                n = n/2
        return True
        """
        Another Solution1:

        return (n>0) and (n & (n-1))==0
        """
        """
        Another Solution2:

        return n > 0 and bin(n).count('1') == 1
        """