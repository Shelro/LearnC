class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for n in nums:
            if n==0:
                nums.remove(n)
                nums.append(n)