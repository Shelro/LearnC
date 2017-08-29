class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        nDics = {}
        for n in nums:
            nDics[n]=nDics.get(n,0)+1
        for key in nDics:
            if nDics[key]>1:
                return True
        return False
        
        """
        Another Method: By myself
     
        if not nums:

            return False

        temp = list(set(nums))

        if len(temp)==len(nums):

            return False

        return True
        """