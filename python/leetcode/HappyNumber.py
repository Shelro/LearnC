class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        My Answer: NOT RIGHT
        
        if n <=0:
            return False
        s = 10
        while s>9:
            temp=[]
            while n>0:
                temp.append(n%10)
                n/=10
            s = 0
            for i in temp:
                s += i**2
            n = s
        if s==1:
            return True
        return False
        """
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True