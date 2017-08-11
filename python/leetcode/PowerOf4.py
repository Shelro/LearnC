class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        sqrtN = int(math.sqrt(num))
        if (sqrtN & (sqrtN-1))==0 and sqrtN**2==num:
            return True
        return False

        """
        Faster Solution:
        
        if num <= 0:
            return False
        
        while num > 1:
            if num % 4 != 0:
                return False
            
            num = num >> 2
        
        return True
        """