class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        s = len(nums[0])*len(nums)
        res = []
        if r*c!=s:
            return nums
        else:
            for i in range(1,len(nums)):
                nums[0].extend(nums[i])
            for j in range(r):
                res.append(nums[0][j*c:(j+1)*c])
            return res