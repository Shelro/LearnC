class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = ['Q','W','E','R','T','Y','U','I','O','P']
        row2 = ['A','S','D','F','G','H','J','K','L']
        row3 = ['Z','X','C','V','B','N','M']
        result = []
        for w in words:
            wlist = list(w.upper())
            f = 0
            isExist = True
            for r in row1:
                if r==wlist[0]:
                    f=1
            if f==0:
                for r in row2:
                    if r==wlist[0]:
                        f=2
            if f==0:
                for r in row3:
                    if r==wlist[0]:
                        f=3
            for i in range(1, len(wlist)):
                isFind = False
                if f==1:
                    for r in row1:
                        if r==wlist[i]:
                            isFind = True
                            break
                elif f==2:
                    for r in row2:
                        if r==wlist[i]:
                            isFind = True
                            break
                elif f==3:
                    for r in row3:
                        if r==wlist[i]:
                            isFind = True
                            break
                else: 
                    break
                if not isFind:
                    isExist = False
                    break
            if isExist:
                result.append(w)
        return result