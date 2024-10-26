"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
        Time: O(n)
        Space:O(n)
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #1. Create hashmap for this operation 
        hashmap = {}
        
        #2. Store new nodes in the hashmap 
        current = head
        
        while current:
            # create the copy first 
            copy = Node(current.val)
            # initialize in the hashmap
            hashmap[current] = copy
            # head to the next item
            current = current.next
        
        #3. Update all the references in this list node 
        secondCurrent = head
        while secondCurrent:
            copyCurrent= hashmap[secondCurrent]
            copyCurrent.next = hashmap[secondCurrent.next] if secondCurrent.next else None
            copyCurrent.random = hashmap[secondCurrent.random] if secondCurrent.random else None
            
            secondCurrent = secondCurrent.next
        #4. Return the head
        return hashmap[head] if  head else None