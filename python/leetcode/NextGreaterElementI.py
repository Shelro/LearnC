class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        if not findNums:
            return []
        for f in findNums:
            m = -1
            index = nums.index(f)
            for i in range(index+1, len(nums)):
                if nums[i]>f:
                    m = nums[i]
                    break
            res.append(m)
        return res