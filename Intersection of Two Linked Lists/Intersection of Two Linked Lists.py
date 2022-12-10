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
        
        head1, head2 = headA, headB
        shortest, longest = headA, headB
        
        while head1 is not None and head2 is not None:
            head1 = head1.next
            head2 = head2.next
            
        if head1 is None:
            shortest = headA
            longest = headB
            
            while head2 is not None:
                head2 = head2.next
                longest = longest.next
    
        elif head2 is None:
            shortest = headB
            longest = headA
            
            while head1 is not None:
                head1 = head1.next
                longest = longest.next
        
        while shortest is not None and longest is not None:
            if shortest == longest:
                return shortest
            
            shortest = shortest.next
            longest = longest.next
            
