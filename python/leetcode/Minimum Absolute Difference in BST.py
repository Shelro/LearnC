# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        temp = [root]
        res = [root.val]
        while temp:
            new_t=[]
            for t in temp:
                if t.left:
                    res.append(t.left.val)
                    new_t.append(t.left)
                if t.right:
                    res.append(t.right.val)
                    new_t.append(t.right)
            temp = new_t
        res.sort()
        result = res[1]-res[0]
        for i in xrange(1,len(res)-1):
            result = min(result,res[i+1]-res[i])
        return result