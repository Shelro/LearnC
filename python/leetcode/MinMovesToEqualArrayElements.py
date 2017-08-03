class Solution(object):
    """
    My Answer: Time Limit Excceed
    def checkEqual(self, nums):
        temp = nums[0]
        for i in range(1, len(nums)):
            if temp!=nums[i]:
                return False
        return True
    
    def minMoves(self, nums):
        if self.checkEqual(nums):
            return 0
        else:
            counts = 0
            while not self.checkEqual(nums):
                nums.sort()
                for j in range(len(nums)-1):
                    nums[j] += 1
                counts += 1
            return counts
        """
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)
