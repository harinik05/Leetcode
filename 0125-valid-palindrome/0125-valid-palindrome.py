class Solution:
    def isPalindrome(self, s: str) -> bool:
        finalString=""
        for character in s:
            if character.isalnum():
                finalString+=character.lower()
    
        if finalString==finalString[::-1]:
            return True
        return False