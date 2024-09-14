from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        #1. Put everything in valid parenthesis 
        hashmap = {}
        
        #2. Put stuff in the hashmap 
        hashmap['}'] = '{'
        hashmap[')'] = '('
        hashmap[']'] = '['
        
        #3. create the stack to keep track of open braces
        stack = []
        
        #4. for each number
        for i, brace in enumerate(s):
            #a. Put in the stack if its an opening brace 
            if brace in hashmap.values():
                stack.append(brace)
            
            #b. what if its a closing brace
            else:
                topElement = stack.pop() if stack else '?'
                if topElement!= hashmap[brace]:
                    return False
                
        
        return not stack