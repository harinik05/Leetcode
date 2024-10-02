from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        #1. Put the proper structures into the hashmap 
        hashmap = defaultdict()
        
        #2. Put some stuff into hashnmap 
        hashmap[')'] = '('
        hashmap['}'] = '{'
        hashmap[']']  = '['
        
        #3. Put stuff in to the stack (LIFO) - stack has openers
        stack = []
        
        #4. Loop thorugh all characters 
        for c in s:
            if c in hashmap.values():
                stack.append(c)
            else:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
        
        #5. return true
        return True if not stack else False
                
        
        