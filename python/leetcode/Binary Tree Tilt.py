# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfTree(self, root):
        if not root:
            return 0
        temp = [root]
        res = 0
        while temp:
            new_t = []
            for t in temp:
                res+=t.val
                if t.left:
                    new_t.append(t.left)
                if t.right:
                    new_t.append(t.right)
                temp=new_t
        return res
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        elif not root.left:
            return abs(self.sumOfTree(root.right))+self.findTilt(root.right)
        elif not root.right:
            return abs(self.sumOfTree(root.left))+self.findTilt(root.left)
        else:
            return abs(self.sumOfTree(root.left)-self.sumOfTree(root.right))+self.findTilt(root.left)+self.findTilt(root.right)