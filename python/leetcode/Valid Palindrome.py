class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        Time Limit Excceed:

        if not s:
            return True
        t = s.lower()
        tlist = t.split(" ")
        slist = []
        for t in tlist:
            slist.extend(list(t))
        i=0
        while i < len(slist):
            if ord(slist[i])<48 or (ord(slist[i])>57 and ord(slist[i])<97) or ord(slist[i])>122:
                slist.remove(slist[i])
            else:
                i+=1
        for i in xrange(len(slist)/2):
            if slist[i]!=slist[len(slist)-1-i]:
                return False
        return True
        """

        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True