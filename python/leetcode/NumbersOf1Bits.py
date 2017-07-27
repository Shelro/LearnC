class Solution(object):
    def turntoBinary(self, x):
        #type x: int
        result = ''
        while x>0:
            rem = x % 2
            x = x / 2
            result = str(rem) + result
        return result
    
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ham = self.turntoBinary(n)
        hamList = list(ham)
        
        counts = 0
        for h in hamList:
            if h=='1':
                counts += 1
                
        return counts