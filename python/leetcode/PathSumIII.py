# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    My Answer: Not right

    def checkPath(self, root, sum):
        if not root:
            return False
        if root.val==sum:
            return True
        else:
            return self.checkPath(root.left,sum-root.val) or self.checkPath(root.right,sum-root.val)
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        if root.val==sum:
            res+=1
        else:
            if self.checkPath(root,sum):
                res+=1
        res += self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
        return res
    """
    def find_paths(self, root, target):
        if root:
            return int(root.val == target) + self.find_paths(root.left, target-root.val) + self.find_paths(root.right, target-root.val)
        return 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.find_paths(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0