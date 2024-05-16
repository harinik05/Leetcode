class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ListNodes for storing odd and even stuff
        oddDummy = ListNode(-1)
        oddCurrent = oddDummy
        
        evenDummy = ListNode(-1)
        evenCurrent = evenDummy
        
        headCpy = head
        
        # Keep track of odd and even indices
        is_odd = True
        
        # while loop 
        while headCpy:
            if is_odd:
                oddCurrent.next = headCpy
                oddCurrent = oddCurrent.next
            else:
                evenCurrent.next = headCpy
                evenCurrent = evenCurrent.next
            headCpy = headCpy.next 
            is_odd = not is_odd
        
        # Terminate the even list
        evenCurrent.next = None
        
        # Connect odd list to even list
        oddCurrent.next = evenDummy.next 
        
        return oddDummy.next
