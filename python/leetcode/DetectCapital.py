class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)==1:
            return True
        wlist = list(word)
        if ord(wlist[0])>=ord('a'):
            for w in wlist[1:]:
                if ord(w)<ord('a'):
                    return False
            return True
        else:
            if len(wlist)==2:
                return True
            if ord(wlist[1])>=ord('a'):
                for w in wlist[2:]:
                    if ord(w)<ord('a'):
                        return False
                return True
            else:
                for w in wlist[2:]:
                    if ord(w)>=ord('a'):
                        return False
                return True
        """
        Faster Solution:

        if word.istitle():
            return True
        if word.islower():
            return True
        if word.isupper():
            return True
        return False
        """