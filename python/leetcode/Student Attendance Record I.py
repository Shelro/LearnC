class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        dic = {}
        slist = list(s)
        Lcounts = 0
        temp = 0
        for i in xrange(len(slist)):
            dic[slist[i]] = dic.get(slist[i],0)+1
            if slist[i]=="L":
                temp+=1
            else:
                Lcounts = max(Lcounts,temp)
                temp=0
        Lcounts = max(Lcounts,temp)
        if dic.get("A"):
            if dic["A"]>1:
                return False
        if Lcounts>2:
            return False
        return True

        """
        Better Solution:

        return not (s.count('A') > 1 or 'LLL' in s)
        """