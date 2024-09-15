from collections import defaultdict

# To find the maximum length of substring, you only need the first and last occurence
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        #1. Keep a variable to keep track of the maximum length 
        maxLength = -1
        
        #2. Create a hashmap to keep track of the first index that it occurs 
        hashmap = {}
        
        #3. Loop thru all the characters 
        for i, character in enumerate(s):
            #a. Determine if the key is in the hashmap 
            if character in hashmap.keys():
                maxLength = max(maxLength, i-hashmap[character]-1)
            else:
                hashmap[character] = i
        
        return maxLength
                
            