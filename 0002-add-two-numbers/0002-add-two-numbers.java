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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        //1. Output list node
        ListNode dummy = new ListNode(-1);
        ListNode resultant = dummy;
        int carry = 0;
        int sum = 0;
        
        //2. While loop
        while(l1!=null || l2!=null||carry!=0){
            //a) initialize the values
            int firstVal = (l1!=null)?l1.val:0;
            int secondVal = (l2!=null)?l2.val:0;
            
            //b) inialize the sum 
            sum = firstVal+ secondVal+carry;
            carry = sum/10;
            resultant.next = new ListNode(sum%10);
            resultant = resultant.next;
            
            
            //c.) go to the next values
            l1 = (l1!=null)?l1.next:null;
            l2 = (l2!=null)?l2.next:null;
            
        }
        return dummy.next;
        
    }
}