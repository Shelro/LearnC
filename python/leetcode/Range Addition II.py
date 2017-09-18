"""
My Answer: Not Right

from numpy import *

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m*n
        M=zeros([m,n])
        temp = 0
        for o in ops:
            for i in xrange(min(m,o[0])):
                for j in xrange(min(n,o[1])):
                    M[i][j]+=1
                    temp = max(M[i][j],temp)
        counts=0
        for i in xrange(min(m,o[0])):
            for j in xrange(min(n,o[1])):
                if M[i][j]==temp:
                    counts+=1
        return counts
"""

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m*n
        return min(op[0] for op in ops)*min(op[1] for op in ops)