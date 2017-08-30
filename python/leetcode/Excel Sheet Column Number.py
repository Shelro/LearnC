class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        slist = list(s)
        res = 0
        for sl in slist:
            res = res*26 + ord(sl)-ord("A")+1
        return res