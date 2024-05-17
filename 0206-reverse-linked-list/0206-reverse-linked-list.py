# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1. if head is none return none 
        if head == None:
            return None
        # Reverse a linked list using cnpc
        currentPointer = head
        previousPointer = None
        
        while currentPointer:
            temp = currentPointer.next 
            currentPointer.next = previousPointer
            previousPointer = currentPointer
            currentPointer = temp
        return previousPointer