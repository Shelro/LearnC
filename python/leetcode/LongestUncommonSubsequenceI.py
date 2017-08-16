class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a)!=len(b):
            return max(len(a),len(b))
        for i in range(len(a)):
            if a[i]!=b[i]:
                return len(a)
        return -1