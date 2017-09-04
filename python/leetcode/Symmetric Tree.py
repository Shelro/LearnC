# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        My Answer: Not right

        if not root:
            return True
        
        temp = [root]
        while temp:
            if len(temp)==1:
                if not temp[0].left and not temp[0].right:
                    return True
                elif temp[0].left and temp[0].right:
                    if temp[0].left.val!=temp[0].right.val:
                        return False
                    temp = [temp[0].left,temp[0].right]
                else:
                    return False
            t1=[]
            t2=[]
            for i in xrange(len(temp)):
                if i<len(temp)/2:
                    if temp[i]:
                        if temp[i].left:
                            t1.append(temp[i].left)
                        else:
                            t1.append(None)
                        if temp[i].right:
                            t1.append(temp[i].right)
                        else:
                            t1.append(None)
                else:
                    if temp[i]:
                        if temp[i].left:
                            t2.append(temp[i].left)
                        else:
                            t2.append(None)
                        if temp[i].right:
                            t2.append(temp[i].right)
                        else:
                            t2.append(None)
            r1=[]
            r2=[]
            for t in t1:
                if not t:
                    r1.append(t)
                else:
                    r1.append(t.val)
            for t in t2:
                if not t:
                    r2.append(t)
                else:
                    r2.append(t.val)
            r1.reverse()
            if r1!=r2:
                return False
        return True
        """

        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        
        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPiar = self.isMirror(left.right, right.left)
            return outPair and inPiar
        else:
            return False