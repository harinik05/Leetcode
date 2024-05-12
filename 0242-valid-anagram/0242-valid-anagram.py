class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # a. Define dictionaries for hashmap
        hashmap_s = {}
        hashmap_t = {}
        
        # b. Loop through the entire string
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            # Update hashmap for string s
            if s[i] not in hashmap_s:
                hashmap_s[s[i]] = 1
            else:
                hashmap_s[s[i]] += 1
            
            # Update hashmap for string t
            if t[i] not in hashmap_t:
                hashmap_t[t[i]] = 1
            else:
                hashmap_t[t[i]] += 1
        
        # c. Check if the two hashmaps are equal
        return hashmap_s == hashmap_t
