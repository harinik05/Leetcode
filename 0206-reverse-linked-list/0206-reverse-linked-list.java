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
    public ListNode reverseList(ListNode head) {
        //Check if the list node is empty 
        if(head == null){
            return null;
        }
        
        ListNode previous = null;
        ListNode current = head;
        //cnpc
        while (current!=null){
            ListNode temp = current.next;
            current.next = previous;
            previous = current;
            current = temp;
        }
        
        return previous;
        
    }
}