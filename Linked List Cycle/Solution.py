# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next or not head.next.next:
            return False
        
        walker, runner = head, head
        
        while walker.next and runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
               
        return False  

