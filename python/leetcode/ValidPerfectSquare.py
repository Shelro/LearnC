class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        first = 1
        last = int(num/2)
        while first<=last:
            mid = int((first+last)/2)
            temp = mid**2
            if temp==num:
                return True
            elif temp>num:
                last = mid-1
            else:
                first = mid+1
        return False
        """
        Faster Solution:

        x=num
        while x*x>num:
            x=(x+num/x)>>1  //Equal to x = (x+num/x)/2
        return x*x==num
        """