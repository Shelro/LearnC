def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        stri = s.split(' ')
        temp = 1
        for i in range(1, len(stri)+1):
            if stri[len(stri)-i]!='':
                temp = i
                break
        if temp==len(stri)+1:
            return 0
        else:
            return len(stri[len(stri)-temp])
        
s = raw_input()
print lengthOfLastWord(s)
