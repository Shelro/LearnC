class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        slist = list(s)
        for i in xrange(len(s)):
            if not dic.get(slist[i]):
                dic[slist[i]]=[i,1]
            else:
                dic[slist[i]][1]+=1
        m = len(s)
        for key in dic:
            if dic[key][1]==1:
                m=min(m,dic[key][0])
        if m==len(s):
            return -1
        else:
            return m
        """
        Faster Solution:

        index = []
        for char in set(s):
            if s.find(char) == s.rfind(char):
                index.append(s.find(char))
        return min(index) if index else -1
        """