class Solution(object):
    """
    My Answer: Time Limit Excceed

    def isDelable(self, n):
        length = int(math.sqrt(n))+1
        for i in range(2, length):
            if n%i==0:
                return True
        return False
    
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        primes = 0
        for i in range(2, n):
            if not self.isDelable(i):
                primes+=1
        return primes
    """
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)