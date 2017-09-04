# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    My Answer: Not right

    def checkNode(self,root,p):
        if not root:
            return False
        if not root.left and not root.right:
            return False
        elif root.left:
            return self.checkNode(root.left,p)
        elif root.right:
            return self.checkNode(root.right,p)
        else:
            return self.checkNode(root.left,p) or self.checkNode(root.right,p)
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if not p or not q:
            return root
        if p==root:
            if self.checkNode(root,q):
                return root
        if q==root:
            if self.checkNode(root,p):
                return root
        if root.left:
            if self.lowestCommonAncestor(root.left,p,q):
                return self.lowestCommonAncestor(root.left,p,q)
        if root.right:
            if self.lowestCommonAncestor(root.right,p,q):
                return self.lowestCommonAncestor(root.right,p,q)
        if self.checkNode(root,p) and self.checkNode(root,q):
            return root
    """
    def lowestCommonAncestor(self, root, p, q):
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root