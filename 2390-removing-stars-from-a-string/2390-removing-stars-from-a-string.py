class Solution:
    def removeStars(self, s: str) -> str:
        # Create a stack 
        stack = []
        
        # For loop 
        for i, character in enumerate(s):
            if character == "*":
                stack.pop()
            else:
                stack.append(character)
        return ''.join(stack)