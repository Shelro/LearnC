class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        slist = list(s)
        res = 0
        i=0
        while i < len(s):
            if slist[i]=="M":
                res+=1000
            elif slist[i]=="D":
                res+=500
            elif slist[i]=="C":
                if i!=len(slist)-1:
                    if slist[i+1]=="D":
                        res+=400
                        i+=1
                    elif slist[i+1]=="M":
                        res+=900
                        i+=1
                    else:
                        res+=100
                else:
                    res+=100
            elif slist[i]=="L":
                res+=50
            elif slist[i]=="X":
                if i!=len(slist)-1:
                    if slist[i+1]=="C":
                        res+=90
                        i+=1
                    elif slist[i+1]=="L":
                        res+=40
                        i+=1
                    else:
                        res+=10
                else:
                    res+=10
            elif slist[i]=="V":
                res+=5
            else:
                if i!=len(slist)-1:
                    if slist[i+1]=="V":
                        res+=4
                        i+=1
                    elif slist[i+1]=="X":
                        res+=9
                        i+=1
                    else:
                        res+=1
                else:
                    res+=1
            i+=1
        return res
        """
        Faster Solution:

        numerals = {'i': 1,
                    'v': 5,
                    'x': 10,
                    'l': 50,
                    'c': 100,
                    'd': 500,
                    'm': 1000}
        
        total = 0
        ascending = True
        s = reversed(s.lower())
        prev_val = 0
        for char in s:
            val = numerals[char]
            if val >= prev_val:
                total += val
            else:
                total -= val
            prev_val = val
        return total
        """