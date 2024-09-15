class Solution:
    def maxVowels(self, s: str, k: int) -> int:
       # Use a sliding window problem approach in this case (but not with left and right pointer)
        
        #1. Initialize the set
        superSet = set()
        
        #2, Put all the vowels in the superset
        superSet.add('a')
        superSet.add('e')
        superSet.add('i')
        superSet.add('o')
        superSet.add('u')
        
        #3. Create a sliding window of k 
        counter = 0
        
        for l in range(k):
            if s[l] in superSet:
                counter+=1
        
        maxAnswer = counter
        
        #4. Loop through all the windows
        for r in range(k,len(s)):
            # Increment the count as you're increasing the right pointer 
            if s[r] in superSet:
                counter+=1
            
            # decrement it since we're moving the left pointer 
            if s[r-k] in superSet:
                counter-=1
            
            # find the maximum
            maxAnswer = max(counter, maxAnswer)
        
        return maxAnswer
            
            
        
       
    
            
            
        
        
    
    