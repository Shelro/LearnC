class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        My Answer: Time Limit Excceed

        if not numbers:
            return None
        for i in range(len(numbers)-1):
            temp = target - numbers[i]
            if temp in numbers[i+1:]:
                num = numbers[i+1:]
                index = num.index(temp)
                return [i+1,index+1+i+1]
        return None
        """
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1