class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        diff = area
        temp = 0
        res = []
        for i in xrange(1,int(math.sqrt(area))+1):
            L = area/i
            if L*i==area:
                temp = L - i
                if diff>temp:
                    res = [L,i]
                    diff = temp
        return res