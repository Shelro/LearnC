class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        first = 1
        last = x
        while (last - first)>1:
            mid = (first + last)/2
            if mid**2>x:
                last = mid
            elif mid**2<x:
                first = mid
            else:
                return mid
        return first
