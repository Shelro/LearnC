class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        if not candies:
            return 0
        can_dic = {}
        for c in candies:
            can_dic[c] = can_dic.get(c,0)+1
        if len(can_dic)>=len(candies)/2:
            return len(candies)/2
        else:
            return len(can_dic)
  
        """
        Faster Solution:
    
        return min(len(set(candies)),len(candies)/2)
        """