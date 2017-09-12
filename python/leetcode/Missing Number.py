class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if not nums:
            return 0
        for i in xrange(len(nums)):
            if nums[i]!=i:
                return i
        return nums[-1]+1

        """
        Better Solution:

        n = len(nums)
        return n * (n+1) / 2 - sum(nums)
        """