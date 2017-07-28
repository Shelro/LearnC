# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        :My code can't work
        :it output the result as [[20,8],9] or [[[20],[8]],[9]]
        result = []
        if root==None:
            return result
        else:
            child = self.levelOrderBottom(root.left) + self.levelOrderBottom(root.right)
            if child!=[]:
                result.append(child)
            result.append(root.val)
            return result
        """

        self.results = []
        if not root:
            return self.results
        q = [root]
        while q:
            new_q = []
            self.results.append([n.val for n in q])
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return list(reversed(self.results))