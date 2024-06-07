# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy 
        
        #1. Loop through everything
        carry = 0
        while(l1 or l2 or carry!=0 ):
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            
            totalSum = l1Val+ l2Val+ carry
            carry = totalSum//10
            
            temp = totalSum%10
            tempNode = ListNode(temp)
            current.next = tempNode
            current = current.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next