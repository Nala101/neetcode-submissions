/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        
        ListNode leftPointer = head;
        
        // Slow fast pointer
        ListNode slow = head;
        ListNode fast = head.next;
        for (; fast != null; ){
            slow = slow.next;
            fast = fast.next;
            if (fast == null){
                break;
            }else{
                fast = fast.next;
            }
        }

        // now slow will be at the middle pointer! 
        // Since it completes it 2x as fast, for the fast pointer
        // to get to the end, it has to be 2x head, so that means the
        // slow pointer is at the half way point 

        // now this here we can reverse the linked list for the second half
        ListNode prev = null;
        ListNode rightPointer = slow;
        for (; rightPointer != null;){
            // we do pointer.next becuase i wanna see when its at the end, not past it
            ListNode temp = rightPointer.next;
            rightPointer.next = prev;
            prev = rightPointer;
            rightPointer = temp;
        }
        rightPointer = prev;
        while(rightPointer.next != null){
            
            // do the left side
            ListNode leftTemp = leftPointer.next;
            leftPointer.next = rightPointer;
            leftPointer = leftTemp;

            // do the right side
            ListNode rightTemp = rightPointer.next;
            rightPointer.next = leftPointer;
            rightPointer = rightTemp;

        }
    }
}
