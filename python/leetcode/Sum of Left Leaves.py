# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        temp = [root]
        while temp:
            new_temp=[]
            for t in temp:
                if t.left:
                    if not t.left.left and not t.left.right:
                        res+=t.left.val
                    else:
                        new_temp.append(t.left)
                if t.right:
                    new_temp.append(t.right)
            temp = new_temp
        return res
        """
        Faster Solution:

        ans=0
        if not root:
            return 0
        if root.left:#has left subtree p
            p=root.left
            if not p.left and not p.right:#p is left leave
                ans+=p.val
            else:#p is not leave
                ans+=self.sumOfLeftLeaves(root.left)
        if root.right:
            ans+=self.sumOfLeftLeaves(root.right)
        return ans
        """