class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        for i in xrange(1,n):
            rlist = list(res)
            s = rlist[0]
            counts = 1
            temp = ""
            for j in xrange(1,len(rlist)):
                if rlist[j]==s:
                    counts+=1
                else:
                    temp+=str(counts)+s
                    counts = 1
                    s = rlist[j]
            temp+=str(counts)+s
            res = temp
        return res