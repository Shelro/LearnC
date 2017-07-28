class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        count = [0] * (N+1)
        for x in nums:
            count[x] += 1
        for x in xrange(1, len(nums)+1):
            if count[x] == 2:
                twice = x
            if count[x] == 0:
                never = x
        return twice, never
    
    """
    Bonus Solution: Suppose x:duplicate one; y: missing one
    def findErrorNums(self, A):
    N = len(A)
    alpha = sum(A) - N*(N+1)/2                                ------------------- x-y
    beta = (sum(x*x for x in A) - N*(N+1)*(2*N+1)/6) / alpha  ------------------- x*x-y*y
    return (alpha + beta) / 2, (beta - alpha) / 2
    """