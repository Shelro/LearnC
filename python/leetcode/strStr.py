class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        elif not haystack:
            return -1
        
        hlist = list(haystack)
        nlist = list(needle)
        
        findHead = False
        notMatch = False
        
        for i in range(len(hlist)-len(nlist)+1):
            if hlist[i] == nlist[0]:
                findHead = True
                notMatch = False
                for j in range(1, len(nlist)):
                    if hlist[i+j] != nlist[j]:
                        notMatch = True
                        break
                if not notMatch:
                    return i
                else:
                    findHead = False
        if not findHead:
            return -1
"""
Another Solution: much faster

class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack: 
            return haystack.index(needle)
        else:
            return -1 
"""