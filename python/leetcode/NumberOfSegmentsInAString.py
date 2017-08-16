class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        #This problem ask us to find how many words in string, not the longest word in string
        """
        My Answer: Not Right

        if not s:
            return 0
        slist = s.split(' ')
        res = 0
        for v in slist:
            if not v:
                return 0
            vlist = list(v)
            if ord(v[-1])<ord('a') or ord(v[-1])>ord('z'):
                res = max(len(v)-1,res)
            else:
                res = max(len(v),res)
        return res
        """
        return len(s.split())