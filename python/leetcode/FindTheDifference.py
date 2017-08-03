class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Can't solve it by myself
        """
        return list((collections.Counter(t) - collections.Counter(s)))[0]
        """
        #Another Solution: Use set, much quicker
        s_set=set(s)
        t_set=set(t)
        if s_set==t_set:
            for i in range(0,len(s)):
                if s.count(s[i])<t.count(s[i]):
                    return s[i]
                    break
        
        
        else:
            dif=t_set-s_set
            dif=list(dif)[0]
            return dif