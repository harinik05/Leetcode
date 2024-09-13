class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        #1. Initialize the variables 
        LENGTH = len(pushed)
        stack = []
        
        #2. Initialize the index 
        p = 0
        
        #3. For loop 
        for number in pushed:
            
            #1. Add to the stack continuously 
            stack.append(number)
            
            #2. While the stack satisfies some conditiosn 
            while stack and popped and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        
        #4. Return if p == LENGTH
        return False if stack else True