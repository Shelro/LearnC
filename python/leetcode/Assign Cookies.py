class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not g or not s:
            return 0
        g.sort()
        s.sort()
        res = 0
        temp = -1
        for c in g:
            for i in xrange(temp+1, len(s)):
                while s[i]<c:
                    i+=1
                    if i==len(s):
                        return res
                res+=1
                temp = i
                break
        return res