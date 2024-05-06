class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Create a matrix to store the dp values
        dpMatrix = [[False for _ in range(len(s))] for _ in range(len(s))]
        longest_palindrome = ""

        # Base case: single characters are palindromes
        for i in range(len(s)):
            dpMatrix[i][i] = True
            longest_palindrome = s[i]

        # Base case: two consecutive same characters are palindromes
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dpMatrix[i][i + 1] = True
                longest_palindrome = s[i:i + 2]

        # General case: for substrings of length > 2
        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dpMatrix[i + 1][j - 1]:
                    dpMatrix[i][j] = True
                    longest_palindrome = s[i:j + 1]

        return longest_palindrome
