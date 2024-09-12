class Solution:
    def removeStars(self, s: str) -> str:
        #1. Define the stack 
        stack = []
        
        #2. Loop thru all the characters and pop and append accordingly
        for character in s:
            if character == "*" and stack:
                stack.pop()
            else:
                stack.append(character)
        
        
        #3. Return the final string
        outputStr = ''.join(stack)
        
        return outputStr
        
        
        