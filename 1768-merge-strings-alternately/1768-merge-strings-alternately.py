class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initiate a while loop that goes through everything
        word1Len = len(word1)
        word2Len = len(word2)
        i=0
        j=0
        result = ""
        # while loop 
        while(i<word1Len or j<word2Len):
            #a. If i is still valid then print that
            if i<word1Len:
                result+=word1[i]
                i+=1
            
            #b. if j is still valid then print that 
            if j<word2Len:
                result+=word2[j]
                j+=1
        
        return result
                
        
                
            
        