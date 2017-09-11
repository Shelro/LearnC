class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxLen = 0
        curLen = 1
        for i in xrange(1,len(nums)):
            if nums[i-1]<nums[i]:
                curLen+=1
            else:
                maxLen = max(maxLen,curLen)
                curLen=1
        maxLen = max(maxLen,curLen)
        return maxLen