# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    MY Answer: Not Right
    def BST2list(self,root,res):
        if not root:
            return res
        else:
            res.append(root.val)
            return list(set(self.BST2list(root.left,res).extend(self.BST2list(root.right,res))))
    
    def convertNode(self,root,temp):
        if not root:
            return 
        count = 0
        for i in xrange(len(temp)):
            if temp[len(temp)-1-i]>root.val:
                count += temp[len(temp)-1-i]
        root.val +=count
        self.convertNode(root.left,temp)
        self.convertNode(root.right,temp)
    
    def convertBST(self, root):
        if not root:
            return root
        temp = self.BST2list(root,[])
        temp.sort()
        self.convertNode(root,temp)
    """
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def reverse(root):
            return reverse(root.right) + [root] + reverse(root.left) if root else []
        for a, b in zip(reverse(root), reverse(root)[1:]):
            b.val += a.val
        return root
        