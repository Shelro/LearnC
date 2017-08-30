class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        """
        My Answer: Time Limit Exceed

        if not nums:
            return []
        rank = 1
        res = [""]*len(nums)
        while max(nums)>=0:
            i = nums.index(max(nums))
            if rank ==1:
                res[i] = "Gold Medal"
            elif rank==2:
                res[i] = "Silver Medal"
            elif rank==3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(rank)
            nums[i] = -1
            rank +=1
        return res
        """
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
        return map(dict(zip(sort, rank)).get, nums)