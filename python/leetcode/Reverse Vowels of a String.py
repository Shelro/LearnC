class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        My Answer: Time Limit Excceed
        if not s:
            return s
        slist = list(s)
        res = ""
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        temp = []
        index = []
        for i in xrange(len(slist)):
            if slist[i] in vowels:
                temp.append(slist[i])
                index.append(i)
        temp.reverse()
        for t in xrange(len(temp)):
            slist[index[t]] = temp[t]
        for i in xrange(len(slist)):
            res += slist[i]
        return res
        """

        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

        """
        Solution 2:
  
        vowels = set(list("aeiouAEIOU"))
        s = list(s)
        ptr_1, ptr_2 = 0, len(s) - 1
        while ptr_1 < ptr_2:
            if s[ptr_1] in vowels and s[ptr_2] in vowels:
                s[ptr_1], s[ptr_2] = s[ptr_2], s[ptr_1]
                ptr_1 += 1
                ptr_2 -= 1
            if s[ptr_1] not in vowels:
                ptr_1 += 1
            if s[ptr_2] not in vowels:
                ptr_2 -= 1
        return ''.join(s)
        """