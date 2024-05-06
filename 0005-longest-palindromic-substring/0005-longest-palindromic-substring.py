class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestSoFar = ""
        # for loop 
        for i in range(len(s)):
            for j in range(i,len(s)):
                temp = s[i:j+1]
                #a. condition for its a palindrome
                if temp == temp[::-1] and len(temp) > len(longestSoFar):
                    longestSoFar = temp
                
        return longestSoFar
                