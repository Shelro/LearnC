class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        res = 0
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                if n<=1:
                    return True
                else:
                    return False
        if flowerbed[0]==0 and flowerbed[1]==0:
            res+=1
            flowerbed[0]=1
        for i in xrange(1, len(flowerbed)-1):
            if flowerbed[i+1]==0 and flowerbed[i-1]==0 and flowerbed[i]==0:
                res+=1
                flowerbed[i]=1
        if flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0:
            res+=1
        if n<=res:
            return True
        return False