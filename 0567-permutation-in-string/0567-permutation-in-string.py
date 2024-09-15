from collections import defaultdict
class Solution:
    def checkIfPermutation(self, inputStr, hashmap):
        #a. Create a freqency map for the input Str
        inputMap = defaultdict(int)
        
        #b. loop through everything 
        for i, character in enumerate(inputStr):
            inputMap[character]+=1
        
        #c. check if its the same 
        return inputMap == hashmap
        
        
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Helper function to check if there is a permutation of string
        
        # Take substrings and call this helper function to check if its a permutation, then return true
        
        #1. Establish the strings
        origStr = s2
        smallStr = s1 
        
        #2. Create the hashmaps 
        hashmap = defaultdict(int)
       
        for i, character in enumerate(smallStr):
            hashmap[character]+=1
        
        #3. Check if its a permutation 
        for i in range(len(origStr)-len(smallStr)+1):
            # Temp string
            tempStr = origStr[i:i+len(smallStr)]
            
            # check the output of this 
            output = self.checkIfPermutation(tempStr,hashmap)
            
            if output== True:
                return True
        
        return False
            