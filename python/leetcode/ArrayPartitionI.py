def arrayPairSum(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        for index in range(len(nums)/2):
            print index
            sum += nums[index*2]
        
        return sum

num=[1,3,4,2]
print arrayPairSum(num)
