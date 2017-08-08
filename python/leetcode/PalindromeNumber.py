class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        xlist = list(str(x))
        for i in range(len(xlist)/2):
            if xlist[i]!=xlist[len(xlist)-1-i]:
                return False
        return True
"""
Faster Solution:

        string = str(x)
        if string == string[::-1]:
            return True
        return False
"""