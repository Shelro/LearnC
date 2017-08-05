def findDisappearedNumbers(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        My Answer: Time Limit Exceed
        res = []
        for miss in range(1, len(nums)+1):
            if  not miss in nums:
                res.append(miss)
        return res
        """
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        """
        Better and Faster solution:
        N = set(nums)
        a = []
        for i in range(1,len(nums)+1):
            if i not in N:
                a.append(i)
        return a
        """

nums = [4,3,2,7,8,2,3,1,1]
print findDisappearedNumbers(nums)
