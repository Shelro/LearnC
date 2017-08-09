# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        first = 0
        while queue:
            tempq = []
            s = 0
            for n in queue:
                s += n.val
            res.append(s*1.0/len(queue))
            for node in queue:
                if node.left:
                    tempq.append(node.left)
                if node.right:
                    tempq.append(node.right)
            queue = tempq
        return res