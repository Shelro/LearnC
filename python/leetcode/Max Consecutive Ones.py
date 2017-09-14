class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        counts = 0
        maxOnes = 0
        for n in nums:
            if n==1:
                counts+=1
            else:
                maxOnes = max(maxOnes,counts)
                counts = 0
        maxOnes = max(maxOnes,counts)
        return maxOnes