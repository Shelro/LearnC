class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        dic = {}
        for n in nums1:
            dic[n]=dic.get(n,0)+1
        res=[]
        for n in nums2:
            if dic.get(n):
                if dic.get(n)==1:
                    dic.pop(n)
                    res.append(n)
                else:
                    dic[n]-=1
                    res.append(n)
        return res