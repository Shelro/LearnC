# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        """
        My Answer: Not right and Not completed

        if not root:
            return None
        if root.val==L:
            if not root.right:
                return None
            else:
                res = TreeNode(L)
                tres = res
                if root.right:
                    temp=[root.right]
                    while temp:
                        for t in temp:
                            tres.right = t
                            tres = tres.right
                            if t.val==R:
                                return res
                return None
        #elif
        """

        if not root:
            return None
        if L > root.val:
            return self.trimBST(root.right, L, R)
        elif R < root.val:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root