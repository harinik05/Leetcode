class Solution:
    def isValid(self, s: str) -> bool:
        # Lets use stacks to do this question
        
        #1. Create a hashmap to describe the structure for this 
        hashmap = {}
        hashmap['}'] = '{'
        hashmap[']'] = '['
        hashmap[')'] = '('
        stack = []
        
        #2. Put all the opening braces in the hashmap
        for character in s:
            # Check if opening brace
            if character in hashmap.values():
                stack.append(character)
            
            # Pop off the stack - closing brace
            else:
                opener = stack.pop() if stack else '*'
                
                if hashmap[character] != opener:
                    return False
        return not stack
                
            