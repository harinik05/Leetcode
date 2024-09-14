class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Two hashmaps for bidirectional mapping
        hashmapS = {}
        hashmapT = {}
        
        # loop through the length of one string 
        for i in range(len(s)):
            if s[i] not in hashmapS.keys() and t[i] not in hashmapT.keys():
                hashmapS[s[i]] = t[i]
                hashmapT[t[i]] = s[i]
            
            elif hashmapS.get(s[i])!=t[i] or hashmapT.get(t[i])!=s[i]:
                return False
        
        return True