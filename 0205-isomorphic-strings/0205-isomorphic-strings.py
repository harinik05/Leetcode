class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Mappings must be birectional 
        
        #a. Initialize the hashmap 
        hashmapS = {}
        hashmapT = {}
        
        #b. Initialize the lengths 
        LENGTHS = len(s)
        LENGTHT = len(t)
        
        # c. check if the lengths are equal 
        if LENGTHS != LENGTHT:
            return False 
        
        #d. Loop through the length of string 
        for i in range(LENGTHS):
            #a. Check if its in hashmap
            if s[i] in hashmapS.keys() and t[i] in hashmapT.keys():
                #a.1) Check if they are matching 
                if not (hashmapS[s[i]] == t[i] and hashmapT[t[i]] == s[i]):
                    return False
            
            #b. check if its one of the key 
            elif s[i] in hashmapS.keys():
                if not (hashmapS[s[i]] == t[i]):
                    return False
                hashmapT[t[i]] = s[i]
            elif t[i] in hashmapT.keys():
                if not(hashmapT[t[i]] == s[i]):
                    return False
                hashmapS[s[i]] = t[i]
            
            
            #c. Not in the hashmap? then add to both 
            else:
                hashmapS[s[i]] = t[i]
                hashmapT[t[i]] = s[i]
        
        return True
                
                