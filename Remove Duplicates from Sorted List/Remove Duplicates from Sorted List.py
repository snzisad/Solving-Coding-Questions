# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        items = set()
        new_head = prev_item = ListNode()
        while head:
            if head.val not in items:
                items.add(head.val)
                prev_item.next = ListNode(head.val)
                prev_item = prev_item.next
                
            head = head.next
            
        return new_head.next