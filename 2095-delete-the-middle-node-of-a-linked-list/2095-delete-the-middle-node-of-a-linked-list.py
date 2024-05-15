# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1. Initalize two duplicates 
        headCpy1 = head
        headCpy2 = head
        
        #2. Determine the length of the linked list 
        length = 0
        while headCpy1:
            length+=1
            headCpy1 = headCpy1.next 
        
        
        #3. Find the middle 
        middle = length//2
        counter = 0
        
        #4. Loop through the thing and skip the middle i
        
        #5. use the sentinel head method
        dummy = ListNode(0,head)
        current = dummy
        while current:
            if counter == middle:
                current.next = current.next.next
            
            current = current.next 
            counter+=1
        
        return dummy.next