class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp = 0
        for i in range(len(digits)):
            temp = temp*10 + digits[i]
        temp += 1
        res = []
        while temp>0:
            res.insert(0,temp%10)
            temp = temp / 10
        return res