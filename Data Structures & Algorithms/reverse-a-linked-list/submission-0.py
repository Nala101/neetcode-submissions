# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None
        
        if head.next is None:
            return head

        prev = None
        pointer = head
        while pointer is not None:
            temp = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = temp

        return prev




        
        

        