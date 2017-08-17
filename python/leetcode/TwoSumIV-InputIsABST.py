# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    def findTarget(self, root, k):
        My Answer: Do not contains the situation when k is the sum of serveral numbers

        if not root:
            return False
        if root.val == k:
            return True
        return self.findTarget(root.left, k-root.val) or self.findTarget(root.right, k-root.val) or self.findTarget(root.left,k) or self.findTarget(root.right, k)
    """

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        return self._findTarget(root, set(), k)
    
    def _findTarget(self, node, nodes, k):
        if not node:
            return False

        complement = k - node.val
        if complement in nodes:
            return True

        nodes.add(node.val)

        return self._findTarget(node.left, nodes, k) or self._findTarget(node.right, nodes, k)

    """
    Faster Solution:

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        past = {}
        node_list = [root]
        for n in node_list:
            if k-n.val in past:
                return True
            else:
                past[n.val] = 1
                if n.left: node_list.append(n.left)
                if n.right: node_list.append(n.right)
        return False
    """