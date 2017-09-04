class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        """
        My Answer: Time Limit Excceed

        if not nums:
            return False
        if k==0:
            return False
        for j in xrange(1,k+1):
            for i in xrange(len(nums)-j):
                if nums[i]==nums[i+j]:
                    return True
        return False
        """

        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False