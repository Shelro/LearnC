# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        res = []
        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                res.append(head.val)
                head = head.next
        res.append(head.val)
        return res