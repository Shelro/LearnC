class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        temp = sorted(nums)
        i = 0
        j = len(nums)-1
        while i<j:
            if temp[i]==nums[i]:
                i+=1
            if temp[j]==nums[j]:
                j-=1
            if temp[i]!=nums[i] and temp[j]!=nums[j]:
                break
        if i==j:
            return 0
        return j-i+1