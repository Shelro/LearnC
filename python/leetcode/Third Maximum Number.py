class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = sorted(list(set(nums)))
        if len(temp)<3:
            return temp[-1]
        else:
            return temp[-3]