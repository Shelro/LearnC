class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        slist = str.split(' ')
        plist = list(pattern)
        pl = {}
        if len(slist) != len(plist):
            return False
        for i in range(len(plist)):
            if not pl.get(plist[i]):
                for key in pl:
                    if pl[key]==slist[i]:
                        return False
                pl[plist[i]]=slist[i]
            else:
                if pl[plist[i]] != slist[i]:
                    return False
        return True