class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        temp = 0
        while k:
            temp = nums.pop()
            nums.insert(0, temp)
            k -=1