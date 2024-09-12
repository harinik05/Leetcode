class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #1. Initialize the array 
        LENGTH = len(temperatures)
        answersArr = [0] * LENGTH
        stack = []
        
        #2. Monotonic stack 
        for i, temperature in enumerate(temperatures):
            #a. While loop 
            
            while stack and temperature>temperatures[stack[-1]]:
                #a. Pop the element ad long as current is greater
                pIndex = stack.pop()
                
                #b. Answers 
                answersArr[pIndex] = i - pIndex
                
            stack.append(i)
        
        return answersArr
                
        
        
        
        
        #1. Keep a counter for this 
        '''
        TEMPERATURES -> [73,74, 75, 71, 69, 72, 76, 73]
        
        ANSWERS -> [1, 1, 4, 2, 1, 1, 0,0]
        
        '''
        '''
        LENGTH = len(temperatures)
        answers = [0] * LENGTH
        threshold = max(temperatures)
        #2. Nested for loop 
        for i in range(LENGTH):
            for j in range(i+1, LENGTH):
                #a. Check if the next ones is greater than 
                if temperatures[j] > temperatures[i]:
                    answers[i] = j-i
                    break
                
        
        #3. Return the answer
        return answers
        '''
                    
                    
        