class Solution:
    def hammingWeight(self, n: int) -> int:
        #1. Find and keep a counter for 1 bits
        counterOneBits = 0
        
        #2. while loop 
        while n!=0:
            counterOneBits+=1
            n&=(n-1)
        
        return counterOneBits
    
        