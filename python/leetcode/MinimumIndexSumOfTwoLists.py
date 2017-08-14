class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        s = len(list1)+len(list2)
        res = []
        for i in range(len(list1)):
            if list1[i] in list2:
                if s > (i + list2.index(list1[i])):
                    res = [list1[i]]
                    s = i + list2.index(list1[i])
                elif s == (i + list2.index(list1[i])):
                    res.append(list1[i])
        return res
        """
        Faster Solution:
        
        d = dict(zip(list1, xrange(len(list1))))
        minsum = len(list1) + len(list2)
        res = []
        
        for i in xrange(len(list2)):
            if list2[i] in d:
                if i + d[list2[i]] < minsum:
                    minsum = i + d[list2[i]] 
                    res = [list2[i]]
                elif i + d[list2[i]] == minsum:
                    res.append(list2[i])
            if i >= minsum:
                break
        return res
        """