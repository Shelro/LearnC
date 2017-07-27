class Solution(object):
    def turntoBinary(self, x):
        #type x: int
        result = ''
        """
        if x<0 or x >= pow(2,31):
            return '2'
        """
        while x>0:
            rem = x % 2
            x = x / 2
            result = str(rem) + result
        return result
    
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dis = x ^ y
        disB = self.turntoBinary(dis)
        disList = list(disB)
        
        hamDis = 0
        for d in disList:
            if d=='1':
                hamDis += 1
        
        return hamDis