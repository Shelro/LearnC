# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        """
        My Answer:Not Right

        if not headA or not headB:
            return None
        temp1=[]
        temp2=[]
        temp = headA
        while temp:
            temp1.insert(temp.val,0)
            temp = temp.next
        temp = headB
        while temp:
            temp2.insert(temp.val,0)
            temp = temp.next
        s = min(len(temp1),len(temp2))
        for i in xrange(s):
            if temp1[i]!=temp2[i]:
                if i==0:
                    return None
                else:
                    return temp1[i-1]
        return temp1[s-1]
        """

        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None

# the idea is if you switch head, the possible difference between length would be countered. 
# On the second traversal, they either hit or miss. 
# if they meet, pa or pb would be the node we are looking for, 
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None