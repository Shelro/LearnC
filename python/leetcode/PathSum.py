# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            if sum==root.val:
                return True
            else:
                return False
        else:
            s = sum-root.val
            return self.hasPathSum(root.left, s) or self.hasPathSum(root.right,s)