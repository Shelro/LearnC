class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        isNegative = False
        if num<0:
            isNegative = True
            num = abs(num)
        stack = []
        while num!=0:
            stack.append(num%7)
            num /= 7
        res = 0
        for i in range(len(stack)):
            res = res*10 + stack[len(stack)-1-i]
        if isNegative:
            return "-"+str(res)
        return str(res)
        """
        Faster Solution:

        if num < 0: return '-' + self.convertToBase7(-num)
        if num < 7: return str(num)
        return self.convertToBase7(num//7) + str(num %7)
        """