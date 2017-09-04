class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = s.split(" ")
        res = ""
        for i in xrange(len(slist)):
            temp = list(slist[i])
            temp.reverse()
            stemp = ""
            for t in temp:
                stemp += t
            res+=stemp
            if i<len(slist)-1:
                res+=" "
        return res