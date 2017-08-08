class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        res = ""
        slists = []
        minSize = len(strs[0])
        for s in strs:
            slists.append(list(s))
            minSize = min(minSize, len(s))

        for i in range(minSize):
            temp = slists[0][i]
            notMatch = False
            for j in range(1, len(slists)):
                if slists[j][i]!=temp:
                    notMatch = True
                    return res
            if not notMatch:
                res += temp
        return res
        """
        Better Solution:

        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
    
        return min(strs)
        """