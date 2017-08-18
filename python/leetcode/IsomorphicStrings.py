class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        Wrong answer for "aa" and "ab"
        if not s and not t:
            return True
        elif not s or not t:
            return False
        if len(s)!=len(t):
            return False
        slist = list(s)
        tlist = list(t)
        temp1=""
        temp2=""
        dic1 = {}
        dic2 = {}
        for i in xrange(len(slist)):
            if not dic1.get(slist[i]):
                dic1[slist[i]] = i+1         //if dic1.get(slist[i])==0, if not dic1.get(slist[i]) will do
            if not dic2.get(tlist[i]):
                dic2[tlist[i]] = i+1
            temp1+=str(dic1[slist[i]])
            temp2+=str(dic2[tlist[i]])
        if temp1==temp2:
            return True
        return False

        """
        Faster Solution:

        f = lambda s: map({}.setdefault, s, range(len(s)))
        return f(s) == f(t)
        """
