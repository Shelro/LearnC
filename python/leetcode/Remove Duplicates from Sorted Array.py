class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        i=1
        while i<length:
            if nums[i]==nums[i-1]:
                nums.remove(nums[i])
                length-=1
            else:
                i+=1
        """
        Better Solution

        curr = 0
        last = None
        for x in nums:
            if x != last:
                nums[curr] = x
                curr += 1
                last = x
                
        return curr
        """