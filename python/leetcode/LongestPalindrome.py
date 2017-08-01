class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        slist = list(s)
        slist.sort()
        alpha = {}
        for si in slist:
            if not alpha.get(si):
                alpha[si] = 1
            else:
                alpha[si] += 1
        haveSingle = False
        result = 0
        for key in alpha:
            if alpha[key] == 1:
                haveSingle = True
            elif alpha[key]%2==1:
                result += alpha[key]-1
                haveSingle = True
            else:
                result += alpha[key]
        if haveSingle:
            result += 1
        return result