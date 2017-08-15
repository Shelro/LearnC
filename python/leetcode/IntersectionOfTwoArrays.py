class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        s1 = collections.Counter(nums1)
        s2 = collections.Counter(nums2)
        temp = list(set(nums2))
        res = []
        for key in temp:
            if min(s1[key],s2[key])>0:
                res.append(key)
        return res