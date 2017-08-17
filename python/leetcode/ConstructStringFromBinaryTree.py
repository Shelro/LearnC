# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        res = ""
        res += str(t.val)
        if t.left and t.right:
            res += "(" + self.tree2str(t.left) + ")" + "(" + self.tree2str(t.right) + ")"
        elif t.right:
            res += "()" + "(" + self.tree2str(t.right) + ")"
        elif t.left:
            res += "(" + self.tree2str(t.left) + ")"
        return res