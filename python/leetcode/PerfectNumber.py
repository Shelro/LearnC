class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=1:
            return False
        res = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num%i==0:
                res += (i + num/i)
        if res == num:
            return True
        else:
            return False