# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        """
        My Answer: RuntimeError: maximum recursion depth exceeded
        if not head:
            return None
        if head.val==val:
            head = head.next
        if head:
            head.next = self.removeElements(head.next, val)
        return head
        """
        dummy = ListNode(-1)
        dummy.next = head
        next = dummy
        
        while next != None and next.next != None:
            if next.next.val == val:
                next.next = next.next.next
            else:
                next = next.next
                
        return dummy.next