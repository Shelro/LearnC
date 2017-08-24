class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not nums1:
            nums1=nums2
        if nums2 and n>0:
            if m>=len(nums1):
                if n>=len(nums2):
                    nums1.extend(nums2)
                else:
                    for i in xrange(n):
                        nums1.append(nums2[i])
            else:
                if n>=len(nums2):
                    if len(nums2)+m<len(nums1):
                        for i in xrange(len(nums2)):
                            nums1[m+i] = nums2[i]
                    else:
                        for i in xrange(len(nums1)-m):
                            nums1[m+i] = nums2[i]
                        nums1.extend(nums2[len(nums1):])
                else:
                    if n+m<len(nums1):
                        for i in xrange(n):
                            nums1[m+i] = nums2[i]
                    else:
                        for i in xrange(len(nums1)-m):
                            nums1[m+i] = nums2[i]
                        nums1.extend(nums2[len(nums1):n])
        nums1.sort()