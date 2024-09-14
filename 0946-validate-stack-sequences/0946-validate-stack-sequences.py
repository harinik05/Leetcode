class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        # Keep adding stuff to the stack until it equals the popped stuff
        stack=[]
        for i,number in enumerate(pushed):
            
            #a. Add the first element into the stack
            stack.append(number)
            
            #b. Check the stack 
            while stack and popped and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        
        return not stack and not popped
            