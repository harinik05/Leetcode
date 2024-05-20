class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        # Loop thru all the elements in s
        for i in range(0, len(s)):
            #1. inserting elements into the stack
            if s[i] !="]":
                stack.append(s[i])
            else:
                #1. Pop the string stuff from the stack 
                substring = ""
                while (stack and stack[-1]!="["):
                    substring= stack.pop()+substring
                stack.pop()
                
                #2. check if there are digits left
                digits = ""
                while(stack and stack[-1].isdigit()):
                    digits = stack.pop() + digits
                
                #3. append the value to the stack
                stack.append(int(digits)*substring)
        
        finalString = ''.join(stack)
        return finalString
    
                    
                
            