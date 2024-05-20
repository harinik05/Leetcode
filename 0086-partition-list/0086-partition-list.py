# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #1. Create some linked lists 
        dummyLeft = ListNode(-1)
        currentLeft = dummyLeft
        
        dummyRight = ListNode(-1)
        currentRight = dummyRight
        
        #2. Go through each element in head
        while head:
            if head.val<x:
                currentLeft.next = head
                currentLeft= currentLeft.next
            else:
                currentRight.next = head
                currentRight = currentRight.next 
            head = head.next 
        
        currentRight.next = None
        currentLeft.next = dummyRight.next 
        return dummyLeft.next
        