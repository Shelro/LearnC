class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        elif not s or not t:
            return False
        else:
            if len(s)!=len(t):
                return False
            slist = list(s)
            tlist = list(t)
            dic = {}
            for se in slist:
                dic[se]=dic.get(se,0)+1
            for te in tlist:
                dic[te]=dic.get(te,0)-1
            for key in dic:
                if dic[key]!=0:
                    return False
            return True

        """
        Faster Solution

         # ## if two words are anagram, there length should be equal
        # from collections import Counter
        # if len(s) == len(t):
        #     s = Counter(s)
        #     t = Counter(t)
        #     if not s-t: return True
        # return False
        
#         
#         # using sorting; 
#         if len(s) ==len(t):
#             return sorted(s) == sorted(t)
#         return False
        
    
    ## using hashing: will deal with all the unigram 
        for i in map(chr, range(97, 123)): ## getting the string representation of int 
            if s.count(i) != t.count(i): 
                return False
        return True
        """