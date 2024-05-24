class Solution:
    
    def helperStrings(self, divisor, stringToForm):
        result = ""
        while len(result) < len(stringToForm):
            result += divisor
        
        return result == stringToForm
    
    def retrieveKeyFromValue(self, value, hashmap):
        for key, val in hashmap.items():
            if val == value:
                return key
        return ""
            
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        dictionary = {}
        # 1. Go through the str1 and find out all the possible divisors
        min_length = min(len(str1), len(str2))
        for i in range(1, min_length + 1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                divisor = str1[:i]
                if self.helperStrings(divisor, str1) and self.helperStrings(divisor, str2):
                    length = len(divisor)
                    dictionary[divisor] = length
        
        if not dictionary:
            return ""
        
        # 2. Find the maximum length among divisors
        max_length = max(dictionary.values())
        
        # 3. Retrieve all divisors with maximum length
        divisors_with_max_length = [key for key, value in dictionary.items() if value == max_length]
        
        # 4. Return the lexicographically smallest divisor
        return min(divisors_with_max_length)
