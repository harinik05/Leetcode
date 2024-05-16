# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ListNodes for storing odd and even stuff
        oddDummy = ListNode(-1)
        oddCurrent = oddDummy
        
        evenDummy = ListNode(-1)
        evenCurrent = evenDummy
        
        headCpy = head
        oddStatus = True
        # while loop 
        while headCpy:
            if not oddStatus:
                evenCurrent.next = headCpy
                evenCurrent = evenCurrent.next
            else:
                oddCurrent.next = headCpy
                oddCurrent = oddCurrent.next
            
            headCpy = headCpy.next 
            oddStatus = not oddStatus
        
        evenCurrent.next = None
        oddCurrent.next = evenDummy.next
        
        # dont leave evenCurrent dangling set to null ptr 
        

        return oddDummy.next
            