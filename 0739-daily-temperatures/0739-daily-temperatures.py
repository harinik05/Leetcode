class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #1. For each temperature that you have heres how its gonna work 
        '''
        Monotonic decreasing stack of indexes 
        
        73 -> put in stack 
        compare with current element 73 (must be warmer then u pop off)
        74 -> warmer [73] = []
        
        '''
        stack = []
        answers = [0] *len(temperatures)
        #0. put the first element in 
        #stack.append(0)
        #1. For loop 
        for i, number in enumerate(temperatures):
            #1. while loop for stacks 
            while stack and temperatures[stack[-1]] < number:
                answers[stack[-1]]=(i-stack[-1])
                stack.pop()
            
            #2. append stuff into the stack 
            stack.append(i)
        return answers
                