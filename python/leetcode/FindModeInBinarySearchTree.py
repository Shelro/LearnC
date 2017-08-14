# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        temp = {}
        q = [root]
        while q:
            new_q = []
            for node in q:
                if not temp.get(node.val):
                    temp[node.val]=1
                else:
                    temp[node.val]+=1
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        m = 0
        res = []
        for key in temp:
            if temp[key]>m:
                res = [key]
                m = temp[key]
            elif temp[key]==m:
                res.append(key)
        return res