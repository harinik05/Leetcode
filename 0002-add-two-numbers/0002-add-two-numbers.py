# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstNum=""
        secondNum = ""
        #1. Loop through the first l1
        while l1:
            firstNum+=str(l1.val)
            l1 = l1.next
        
        #2. loop through the second l2
        while l2:
            secondNum+=str(l2.val)
            l2 = l2.next 
        
        #3. reverse and add the numbers
        firstNum=firstNum[::-1]
        secondNum = secondNum[::-1]
        sumOfNums = int(firstNum) + int(secondNum)
        sumOfNums = str(sumOfNums)
        sumOfNums = sumOfNums[::-1]
        
        #4. store this as a linked list
        dummy = ListNode()
        current = dummy
        for nums in sumOfNums:
            current.next=ListNode(int(nums))
            current=current.next
        
        return dummy.next
            
        