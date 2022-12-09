class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        list3 = head = ListNode()
        while list1 is not None and list2 is not None:
            if list1.val<list2.val:
                list3.next = ListNode(list1.val)
                list1 = list1.next
            else:
                list3.next = ListNode(list2.val)
                list2 = list2.next
                
            list3 = list3.next
            
        while list1 is not None:
            list3.next = ListNode(list1.val)
            list1 = list1.next
            list3 = list3.next
            
        while list2 is not None:
            list3.next = ListNode(list2.val)
            list2 = list2.next
            list3 = list3.next
            
        return head.next