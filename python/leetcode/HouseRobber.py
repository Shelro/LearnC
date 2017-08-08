class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        My Answer: Can't get best result
        if not nums:
            return 0
        
        undercase = []
        amount = 0
        isEnough = False
        while not isEnough:
            i = nums.index(max(nums))
            if not i in undercase:
                amount += nums[i]
                if i>0 and not (i-1) in undercase:
                    undercase.append(i-1)
                if i<len(nums)-1 and not (i+1) in undercase:
                    undercase.append(i+1)
            nums[i]=0
            if max(nums)==0:
                isEnough = True
        return amount
        """
        last, now = 0, 0
        for i in nums: 
            last, now = now, max(last + i, now)
        return now