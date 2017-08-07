class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        """
        My Answer: Not right
        if not ransomNote:
            return True
        elif not magazine:
            return False
        rlist = list(ransomNote)
        mlist = list(magazine)
        for i in range(len(mlist)-len(rlist)+1):
            notMatch = False
            if rlist[0]==mlist[i]:
                for j in range(1,len(rlist)):
                    if rlist[j]!=mlist[i+j]:
                        notMatch = True
                if not notMatch:
                    
                    return True
        return False    
        """
        # This problem means that letters in ransomNote can be contains in magazine
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
        """
        Another Faster Solution:

        for e in set(ransomNote):
            if ransomNote.count(e) > magazine.count(e):
                return False
        return True
        """