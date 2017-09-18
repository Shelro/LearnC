# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        My Answer; Not right

        if not root:
            return -1
        if not root.right:
            return -1
        minV = root.val
        secV = 2**31
        temp=[]
        if root.left:
            temp.append(root.left)
        temp.append(root.right)
        while temp:
            for t in temp:
                new_t = []
                if t.val >minV:
                    secV = min(t.val,secV)
                if t.left:
                    new_t.append(t.left)
                if t.right:
                    new_t.append(t.right)
            temp = new_t
        if secV==minV or secV==2**31:
            return -1
        return secV
        """

        res = [float('inf')]
        def traverse(node):
            if not node:
                return
            if root.val < node.val < res[0]:
                res[0] = node.val
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return -1 if res[0] == float('inf') else res[0]