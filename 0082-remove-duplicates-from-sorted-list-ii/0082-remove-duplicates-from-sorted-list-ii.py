# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1. Create sentinel/dummy 
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        headCpy = head
        
        #2. Loop through the entire linked list
        while headCpy:
            #1. check for duplicates
            if headCpy.next and headCpy.val == headCpy.next.val:
                while headCpy.next and headCpy.val == headCpy.next.val:
                    headCpy = headCpy.next 
                current.next = headCpy.next
            
            # no duplicates
            else:
                current = current.next 
            headCpy = headCpy.next 
        
        return dummy.next
                