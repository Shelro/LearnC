class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        nlist = list(str(num))
        while len(nlist)>1:
            temp = 0 
            for i in nlist:
                temp += int(i)
            num = temp
            nlist = list(str(num))
        return num

        """
        Faster Solution:
  
         while(num >= 10):
            temp = 0
            while(num > 0):
                temp += num % 10
                num /= 10
            num = temp
        return num
        """