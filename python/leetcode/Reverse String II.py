class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        """
        My Answer: Not right

        times = len(s)/k
        if times<1:
            return s[::-1]
        elif times<=2:
            temp = s[0:k]
            res = temp[::-1]+s[k:len(s)]
            return res
        else:
            res = ""
            for i in xrange(times/2):
                temp = s[i*2*k:i*2*k+k]
                res+=temp[::-1]+s[i*2*k+k:(i+1)*2*k]
            if len(s)-(times/2)*2*k<k:
                res+=s[(times/2)*2*k:len(s)]
            else:
                temp = s[(times/2)*2*k:(times/2)*2*k+k]
                res += temp[::-1]+s[(times/2)*2*k+k:len(s)]
        return res
        """

        #Solution 1:
        s = list(s)
        for i in xrange(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
       
        """
        Solution 2:
        
        return s[:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k) if s else ""
        """

        """
        Solution 3:

        news = ''
        n = (len(s) // (2 * k)) * 2 * k
        for i in range(0, n, 2 * k):
            news += s[i:i + k][::-1]
            news += s[i + k:i + 2 * k]
        if len(s) - n < k:
            news += s[n:][::-1]
        else:
            news += s[n:n + k][::-1]
            news += s[n + k:]
        return news
        """