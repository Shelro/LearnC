class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        My Answer: Time Limit Excceed

        nums.sort()
        temp = sorted(list(set(nums)))
        length = 0
        minLen = 0
        maxLen = 0
        
        for i in range(len(temp)-1):
            if temp[i]+1 in temp:
                for j in range(len(nums)):
                    if nums[j]<temp[i] and temp[i]==nums[j+1]:
                        minLen = j+1
                    if nums[j]==temp[i+1]:
                        maxLen = j+1
                length = max(maxLen - minLen, length)
        return length
        """
        count = collections.Counter(nums)
        ans = 0
        for x in count:
            if x+1 in count:
                ans = max(ans, count[x] + count[x+1])
        return ans
        
        """
        Faster Solution:
        
        store = dict()
        for num in nums:
            store[num] = 1 if num not in store else store[num] + 1
        ans = 0
        for num in store:
            if num + 1 in store:
                if store[num] + store[num+1] > ans:
                    ans = store[num] + store[num + 1]
        return ans
        """