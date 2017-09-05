class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        maxLen = int(len(nums)*1.0/2)
        dic = {}
        majority = 0
        N = 0
        for n in nums:
            dic[n] = dic.get(n,0)+1
        for key in dic:
            if dic[key]>=maxLen:
                if majority< dic[key]:
                    majority = dic[key]
                    N = key
        return N

        """
        Faster Solution:

        sorted_nums = sorted(nums)
        array_len = len(nums)
        majority_element = sorted_nums[array_len/2]
            
        return majority_element
        """