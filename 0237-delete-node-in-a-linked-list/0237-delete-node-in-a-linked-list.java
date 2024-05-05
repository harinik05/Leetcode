/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        //1. Set the value of the current to the next
        node.val=node.next.val;
        
        //2. Skip the pointer to the next one
        node.next= node.next.next;
        
        
    }
}