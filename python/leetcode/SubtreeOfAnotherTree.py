# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        """ 
        Wrong answer for [3,4,5,1,null,2] and [3,1,2]
        
        if not s and not t:
            return True
        elif not s or not t:
            return False
        if s.val==t.val:
            return self.isSubtree(s.left, t.left) and self.isSubtree(s.right, t.right) or (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        """
        
        def isMatch(self, s, t):
            if not(s and t):
                return s is t
            return (s.val == t.val and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right))
    
        def isSubtree(self, s, t):
            if self.isMatch(s, t): 
                return True
            if not s: 
                return False
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
       """
       Faster Solution:
       
       def convert(p):
            return '~' + str(p.val) + '$' + convert(p.left) + convert(p.right) if p else '&'
       return convert(t) in convert(s)
       """