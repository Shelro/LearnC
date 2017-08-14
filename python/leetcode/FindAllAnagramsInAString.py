class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        """
        My Answer: Time Limit Excceed

        pd = {}
        slist = list(s)
        plist = list(p)
        for e in plist:
            if not pd.get(e):
                pd[e]=1
            else:
                pd[e]+=1
        res = []
        for i in range(len(slist)-len(plist)+1):
            if pd.get(slist[i]):
                sub = slist[i:i+len(plist)]
                sd = {}
                for e in sub:
                    if not sd.get(e):
                        sd[e]=1
                    else:
                        sd[e]+=1
                notMatch = False
                for key in sd:
                    if pd.get(key) != sd[key]:
                        notMatch = True
                if not notMatch:
                    res.append(i)
        return res
        """
        res = []
        pCounter = collections.Counter(p)
        sCounter = collections.Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
                res.append(i-len(p)+1)   # append the starting index
            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res
        """
        Faster Solution:

        d = {}
        for c in p:
            d[c] = d.get(c, 0) + 1
        store = dict(d)
        
        lo, hi = 0, 0
        m, n = len(s), len(p)
        res = []
        
        while hi < m:
            if s[hi] in d and d[s[hi]] > 0:
                d[s[hi]] -= 1
                hi += 1
                if hi - lo == n:
                    res += [lo]
                    d[s[lo]] += 1
                    lo += 1
            elif s[hi] not in d:
                lo = hi = hi + 1
                d = dict(store)
            else:
                d[s[lo]] += 1
                lo += 1
                
        return res
        """