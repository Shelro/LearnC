class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        My Answer: Time Limit Excceed

        if not s:
            return s
        slist = list(s)
        slist.reverse()
        res = ""
        for i in slist:
            res+=i
        return res
        """

        return s[::-1]