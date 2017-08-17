class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        """
        My Answer: Time Limit Excceed

        if not nums:
            return float(0)
        s = 0
        for i in range(k):
            s += nums[i]
        start = 0
        for i in range(1, len(nums)-k+1):
            temps = 0
            for j in range(k):
                temps += nums[i+j]
            if temps > s:
                s = temps
                start = i
        return float(s*1.0/k)
        """

        P = [0]
        for x in nums:
            P.append(P[-1] + x)
            
        ma = max(P[i+k] - P[i] for i in xrange(len(nums) - k + 1))
        return ma / float(k)

        """
        Faster Solution:
        ret = sum(nums[:k])
        cur = ret
        for i in xrange(k, len(nums)):
            cur = cur - nums[i - k] + nums[i]
            if cur > ret:
                ret = cur
        
        return ret / float(k)
        """