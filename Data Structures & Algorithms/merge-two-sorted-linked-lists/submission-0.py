# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # attempted to do a recursive case first but couldnt figure it out that fast

        if list1 is None:
            return list2
        if list2 is None:
            return list1
        # attempt with while loop
        current = None
        

        if list1.val <= list2.val:
            current = list1
            list1 = list1.next
        else:
            current = list2
            list2 = list2.next

        head = current

        while list1 is not None and list2 is not None:
            
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        
        if list1 is None:
            current.next = list2
        
        if list2 is None:
            current.next = list1

        return head

            


