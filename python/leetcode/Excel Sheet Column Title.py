class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<=0:
            return ""
        res = ""
        while n>0:
            m = n%26
            n = n/26
            if m==0:
                res = "Z"+res
                n-=1
            else:
                res = chr(ord("A")+m-1) + res
        return res

        """
        Faster Solution:

        mp = {i:chr(i+64) for i in xrange(1, 27)}
        res = []
        while n:
            res.append(n % 26 if n % 26 > 0 else 26)
            n = (n-1) // 26
        return ''.join(mp[i] for i in reversed(res))
        """