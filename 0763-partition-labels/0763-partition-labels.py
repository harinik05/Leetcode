class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #1. Create a hashmap to store the last index of the following 
        lastIndexHM = {}
        
        #2. Loop through the entire string 
        for i,character in enumerate(s):
            lastIndexHM[character] = i
        
        
        #3. Loop through the entire string and initialize the arry and sizes
        size = 0
        outputArr = []
        end = 0
        
        for i, character in enumerate(s):
            # Initialize the end 
            end = max(end, lastIndexHM[character])
            
            # Size incrementing 
            size+=1
            
            # if it reaches end:
            if i == end:
                outputArr.append(size)
                size = 0
        
        #4. return the outputArr
        return outputArr
                
            