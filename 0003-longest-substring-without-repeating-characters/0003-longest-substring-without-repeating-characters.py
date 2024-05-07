class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #1. Initialize the output variables 
        outputStr = ""
        length = 0
        seen = set()
        
        #2. Two pointers 
        left = 0
        right = 0
        
        while right<len(s):
            #a. check if the character is not in right set
            if s[right] not in seen:
                seen.add(s[right])
                right+=1
                length=max(length,right-left)
            else:
                seen.remove(s[left])
                left+=1
        return length