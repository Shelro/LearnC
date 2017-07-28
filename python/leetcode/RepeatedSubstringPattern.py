class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        slist = list(s)
        for ii in range(1,length/2+1):
            i = length/2+1-ii
            if length%i==0:
                st = slist[0:i]
                isFound = True
                for j in range(1, length/i):
                    temp = slist[j*i:(j+1)*i]
                    if temp!=st:
                        isFound = False
                        break
                if isFound:
                    return True
        return False