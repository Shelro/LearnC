class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        if k<0:
            return 0
        else:    
            dic={}
            for n in nums:
                dic[n]=dic.get(n,0)+1
            res = 0
            for key in dic:
                if k==0:
                    if dic.get(key)>1:
                        res+=1
                else:
                    if dic.get(key+k):
                        res+=1
            return res