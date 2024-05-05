# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #1. Set the current value to the next node since deletion
        node.val = node.next.val
        
        #2. The next pointer of current node should skip one
        node.next = node.next.next
        