class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counts = 0
        for n in nums:
            if n==val:
                counts+=1
        for i in range(counts):
            nums.remove(val)
        return len(nums)