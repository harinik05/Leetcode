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
        //1. Get the middle of the list
        ListNode slowPtr = head;
        ListNode fastPtr = head;

        while((fastPtr!=null) && (fastPtr.next!=null)){
            slowPtr = slowPtr.next;
            fastPtr = fastPtr.next.next;
        }

        ListNode secondHalf = slowPtr;

        //2. Reverse the entire list
        ListNode previous = null;
        while(secondHalf!=null){
            ListNode temporaryBuffer = secondHalf.next;
            secondHalf.next = previous;
            previous = secondHalf;
            secondHalf = temporaryBuffer;
        }

        ListNode reversedSecondHalf = previous;

        //3. Add into a dummy and set this to head
        ListNode dummyReturn = new ListNode(-1);
        ListNode returnedNode = dummyReturn;
        ListNode original = head;
        int counter = 1;
        while((reversedSecondHalf!=null) && (original!=null)){
            if(counter%2==0){
                returnedNode.next = reversedSecondHalf;
                reversedSecondHalf = reversedSecondHalf.next;
            }else{
                returnedNode.next = original;
                original = original.next;
            }

            //counter
            counter+=1;
            returnedNode = returnedNode.next;
        }
        head = dummyReturn.next;

        
    }
}