class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = ''
        n = num
        while num>0:
            rem = num % 2
            num = num / 2
            result = str(rem) + result
        com = 0
        for i in range(len(result)):
            com += pow(2,i)
        return n^com